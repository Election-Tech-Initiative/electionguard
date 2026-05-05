#!/usr/bin/env python3
"""Generate ElectionGuard sample data from checked-in sample manifests."""

from __future__ import annotations

import argparse
import logging
import os
import shutil
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterable, List


SUPPORTED_MANIFESTS = ("minimal", "small", "full", "hamilton-general")
DEFAULT_VERSION = "0.95.0"
DEFAULT_MANIFEST_DIR = Path("data/sample/manifests")
DEFAULT_OUTPUT_DIR = Path("data/sample/generated")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate sample data from the sample manifests.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--manifest-dir",
        type=Path,
        default=DEFAULT_MANIFEST_DIR,
        help="Directory containing manifests grouped by version.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory where generated sample data is written.",
    )
    parser.add_argument(
        "--version",
        default=DEFAULT_VERSION,
        help="Sample manifest version to generate.",
    )
    parser.add_argument(
        "--manifest",
        action="append",
        choices=SUPPORTED_MANIFESTS,
        help="Manifest name to generate. Can be provided more than once.",
    )
    parser.add_argument(
        "--number-of-ballots",
        type=int,
        default=5,
        help="Number of ballots to generate per manifest.",
    )
    parser.add_argument(
        "--spoil-rate",
        type=int,
        default=50,
        help="Approximate percentage of ballots to spoil instead of cast.",
    )
    parser.add_argument(
        "--all-guardians",
        action="store_true",
        help="Use all guardians during decryption.",
    )
    parser.add_argument(
        "--private-data",
        action="store_true",
        help="Include private test data such as plaintext ballots and guardian keys.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove the output version directory before generating.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show verbose output from the ElectionGuard generator.",
    )
    return parser.parse_args()


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def import_generator():
    try:
        from electionguard.manifest import Manifest
        from electionguard.serialize import from_file
        from electionguard_tools.factories.election_factory import ElectionFactory
        from electionguard_tools.scripts.sample_generator import (
            ElectionSampleDataGenerator,
        )
    except ImportError as exc:
        fail(
            "sample generation requires electionguard-python. "
            "Install it with "
            "`python -m pip install electionguard==1.4.0 dacite==1.6.0 hypothesis`. "
            f"Original import error: {exc}"
        )

    return ElectionFactory, ElectionSampleDataGenerator, Manifest, from_file


def build_manifest_directory_factory(election_factory_class, manifest_class, from_file):
    class ManifestDirectoryElectionFactory(election_factory_class):
        def __init__(self, manifest_data_dir: Path) -> None:
            super().__init__()
            self.manifest_data_dir = manifest_data_dir

        def get_manifest_from_filename(self, filename: str):
            return from_file(manifest_class, str(self.manifest_data_dir / filename))

    return ManifestDirectoryElectionFactory


def copy_manifest_sources(
    manifest_dir: Path, version: str, manifest_names: Iterable[str], package_data_dir: Path
) -> List[str]:
    copied: List[str] = []
    version_dir = manifest_dir / version
    if not version_dir.exists():
        fail(f"manifest version directory does not exist: {version_dir}")

    for manifest_name in manifest_names:
        source = version_dir / f"{manifest_name}.json"
        if not source.exists():
            fail(f"sample manifest does not exist: {source}")

        shutil.copyfile(source, package_data_dir / f"manifest-{manifest_name}.json")
        copied.append(manifest_name)

    return copied


def generate_manifest(
    generator_class,
    election_factory_class,
    manifest_data_dir: Path,
    output_root: Path,
    version: str,
    manifest_name: str,
    number_of_ballots: int,
    spoil_rate: int,
    all_guardians: bool,
    private_data: bool,
) -> None:
    destination = output_root / version / manifest_name
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    with TemporaryDirectory() as work_dir_name:
        work_dir = Path(work_dir_name)
        previous_cwd = Path.cwd()
        try:
            os.chdir(work_dir)
            generator = generator_class()
            generator.election_factory = election_factory_class(manifest_data_dir)
            generator.generate(
                number_of_ballots=number_of_ballots,
                spoil_rate=spoil_rate,
                use_all_guardians=all_guardians,
                use_private_data=private_data,
                sample_manifest=manifest_name,
            )
        finally:
            os.chdir(previous_cwd)

        for generated_dir_name in ("election_record", "election_private_data"):
            generated_dir = work_dir / generated_dir_name
            if generated_dir.exists():
                shutil.copytree(generated_dir, destination / generated_dir_name)


def main() -> None:
    args = parse_args()
    if args.spoil_rate < 0 or args.spoil_rate > 100:
        fail("--spoil-rate must be between 0 and 100")
    if args.number_of_ballots < 1:
        fail("--number-of-ballots must be at least 1")
    if not args.verbose:
        logging.disable(logging.INFO)

    manifest_names = args.manifest or list(SUPPORTED_MANIFESTS)
    output_dir = args.output_dir
    version_output_dir = output_dir / args.version

    if args.clean and version_output_dir.exists():
        shutil.rmtree(version_output_dir)

    (
        election_factory_class,
        generator_class,
        manifest_class,
        from_file,
    ) = import_generator()

    with TemporaryDirectory() as data_dir_name:
        data_dir = Path(data_dir_name)
        copied = copy_manifest_sources(
            args.manifest_dir, args.version, manifest_names, data_dir
        )
        manifest_directory_factory = build_manifest_directory_factory(
            election_factory_class, manifest_class, from_file
        )

        for manifest_name in copied:
            print(f"Generating {args.version}/{manifest_name}")
            generate_manifest(
                generator_class,
                manifest_directory_factory,
                data_dir,
                output_dir,
                args.version,
                manifest_name,
                args.number_of_ballots,
                args.spoil_rate,
                args.all_guardians,
                args.private_data,
            )


if __name__ == "__main__":
    main()
