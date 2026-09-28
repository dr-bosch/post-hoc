# Atom build and update procedure

This document explains how to invoke the atom build, what it processes, and
how to use its timestamped status report when the repository changes.

## What the build does

The build supports two modes. A **full rebuild** reads the authoritative
scope in [`atom-build-manifest.json`](atom-build-manifest.json), parses every
eligible file, and replaces the generated exports. An **incremental sync**
compares file fingerprints with the last saved build status, reparses only
changed or newly added parser inputs, removes records belonging to deleted
inputs, and retains records from unchanged inputs.

Both modes update:

- `atoms.json`
- `atoms.csv`
- `atoms.md`
- `build/atom-build-status.md`
- `build/atom-build-status.json`

The manifest is the master list specification. Its patterns define what is
in scope; the status report expands them into the exact discovered filenames
for each run. New matching files are included without manually maintaining a
second file list.

The build has two limited extraction modes:

1. **Structured HTML atoms:** reads `**/index.html` pages and extracts
   explicitly authored `.atom`, `.fsd-class`, and `.chrono` blocks.
   Evidence-tagged paragraphs inside one `.atom` block are emitted as
   separate records. `.fsd-class` panels are exported as `FSD_PANEL` records;
   extraction does not validate that the classification is supported.
2. **Ontology term occurrence search:** searches eligible Markdown and HTML
   documents for literal FSD class identifiers or labels. Such records use
   `type: TERM`; they are occurrences only, not FSD classifications,
   observations, or proof that a class applies.

This is not an automatic semantic atomizer. It does not read PDF contents,
derive propositions from arbitrary source files, verify citations, or decide
evidence status. A new or edited primary source still requires human review
and atomization following `CLAUDE.md` and, for normative material,
`corpus/laws-and-codes/manual.html`.

## Run the build on your computer

### First time only

Open a terminal in the repository folder and install the build dependency:

```sh
python3 -m pip install -r requirements-build.txt
```

### First build after installing or updating the build process

Run a full rebuild once to establish the fingerprint baseline used by future
syncs:

```sh
./build-atoms.sh
```

### Whenever you change repository files

To sync only the changed inputs:

```sh
./sync-atoms.sh
```

The sync uses the last `build/atom-build-status.json` and `atoms.json` as its
baseline. Keep those generated files available locally between syncs. If the
manifest, parser, or ontology changes, sync stops and asks for a full rebuild;
this avoids applying incremental updates under a changed extraction contract.

To deliberately reprocess every file instead:

```sh
./build-atoms.sh
```

Both commands can be run from the repository folder or called by script path
from another working directory. You can also use `./build-atoms.sh --sync`;
`sync-atoms.sh` is the shorter, purpose-specific command. Do not edit the
generated `atoms.*` files yourself.

When it finishes, review `build/atom-build-status.md`. It shows when the build
ran, which in-scope files changed, record counts, and which source or
analytical files need manual review. The same information is also available
in `build/atom-build-status.json`.

### When changing build code or the extraction contract

Run the test suite before rebuilding:

```sh
python3 -m unittest discover -s tests -v
./build-atoms.sh
```

To report changes against a particular Git revision, pass that revision:

```sh
./build-atoms.sh --base-ref <git-revision>
```

The status report identifies the build mode, content changes, record counts,
and manual-review items. A sync updates only parser-supported inputs; it does
not mean new or changed sources have been semantically atomized.

## Update or add files

1. Add or edit the source or analytical file in its appropriate repository
   layer. Do not edit generated `atoms.*` files by hand.
2. Run `./sync-atoms.sh` to update changed inputs, or
   `./build-atoms.sh` to reprocess the full manifest scope.
3. Inspect the status report. Confirm that the changed/new file appears in
   the input inventory and, where applicable, the manual-review queue.
4. For a new or edited source document, verify provenance and extract
   traceable atoms manually. Add them to the appropriate analytical page or
   workflow according to the repository protocol; do not treat a `TERM`
   record as an atom.
5. Review `atoms.json`, `atoms.csv`, and `atoms.md` for unexpected changes,
   duplicate passages, ambiguous term matches, and correct evidence labels.
6. Include the generated exports and status report with the substantive
   repository update when those outputs are intended to be versioned.

The manifest controls parser scope. Update it when adding a new supported
file type or extraction mode; otherwise, patterns automatically include new
files that match the existing scope. Exclusions keep generated outputs and
method/ontology master files from being reprocessed as source material.

## GitHub Actions: sync or full rebuild

On pushes to `main`, the workflow syncs changed inputs against the saved state.
If no compatible state is cached yet, it performs a full build to establish
the baseline. Afterward it saves the updated state for later runs.

To choose a mode yourself:

1. Open the repository on GitHub and select **Actions**.
2. Select **Deploy to GitHub Pages** from the workflow list.
3. Select **Run workflow**.
4. Choose the branch to build, normally `main`.
5. In **build_mode**, choose **sync** for changed inputs or **full** to
   reprocess the entire manifest scope.
6. Select **Run workflow** to start it.

The workflow restores the most recent atom build state for that branch before
a sync, then saves the updated state for the next run. If no compatible
baseline exists, choose **full** first. Exports and status reports are
included in the Pages artifact; the workflow does not commit them to the
branch.

The build timestamp is generated at execution time in UTC. The report is a
build record and review trigger, not evidence about the institutional events
described by the repository. A sync with no changed inputs retains the current
records and records that no in-scope content changes were detected.

## Scope and evidence safeguards

- `atom-build-manifest.json` is the sole scope reference used by the build
  script.
- `CLAUDE.md` is excluded from the atom input inventory and parser inputs.
  It remains listed as a build-control file so its changes can be reported;
  that tracking does not extract its contents.
- Incremental sync requires a prior build status and export. If no compatible
  baseline is available, run a full rebuild first.
- Literal ontology mentions are recorded as `TERM`, not `FSD`.
- Extracting an authored `.fsd-class` panel produces an `FSD_PANEL` record;
  it preserves the label but does not independently validate its application.
- Search misses, absent passages, and unparsed files are not evidence that an
  event did not occur.
- Do not send credentials or non-public source material to external services
  as part of atomization.
- Do not infer recurrence, legal effect, intent, or system function from
  term frequency.
