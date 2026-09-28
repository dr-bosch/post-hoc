# MCP Server Configuration — Technical Assessment

**Assessment date:** 2026-09-28  
**Configuration assessed:** `.vscode/mcp.json`  
**Purpose:** explain the configured servers in plain language, summarize their authentication and reachability status, and distinguish verified capabilities from assumptions.

## Executive summary

The configuration lists three remote MCP endpoints:

| Configured name | Plain-language description | Authentication / credentials | Connection check |
|---|---|---|---|
| `ckan` | Search public-data portals for datasets, organizations, metadata, and tabular data. | The project describes the hosted endpoint as requiring no authentication. | MCP `initialize`, tool discovery, and several `tools/call` requests succeeded. A portal-discovery tool failed with a server-side compatibility error; direct queries to `data.gov.ie` worked. |
| `ansvar` | Search legislation, regulations, standards, and related regulatory material; retrieve specific provisions or decisions with citations. | Ansvar's setup documentation describes browser-based OAuth 2.1 sign-in and says no API key needs to be pasted. | Responded to an unauthenticated HTTP GET with `401`, consistent with an endpoint requiring authentication. No OAuth flow or MCP handshake was completed. |
| `irish-competition` | The name suggests an Irish competition-law service, but its actual scope and tools could not be verified from an authoritative source during this assessment. | Not verified. The JSON contains no credential configuration. | DNS lookup for `mcp.ansvar.eu` failed during the check; the endpoint was not reached. |

The configuration entries are not proof that a server is continuously connected to this Copilot CLI session. In this research run, CKAN was contacted directly using MCP JSON-RPC; the successful exchange establishes that this endpoint and its tested tools responded at that time, not that an always-on connection exists. The checks did not send credentials.

## Configuration observed

`.vscode/mcp.json` defines the following HTTP endpoints:

- `ckan` — `https://ckan-mcp-server.andy-pr.workers.dev/mcp`
- `ansvar` — `https://gateway.ansvar.eu/mcp`
- `irish-competition` — `https://mcp.ansvar.eu/irish-competition/mcp`

The file contains endpoint URLs only. It does not contain passwords, bearer tokens, API keys, OAuth tokens, or references to credential environment variables.

## Per-server assessment

### CKAN

**Plain language:** Ask an assistant to find datasets on CKAN-based open-data portals, inspect dataset metadata and organizations, and query supported tabular data without needing to know the CKAN API.

The server's project documentation describes the hosted endpoint as public and unauthenticated. It notes that the hosted service has a shared request quota; the project's README currently describes a shared quota of 100,000 requests per day. Quotas and service behavior can change, so check the project documentation before relying on those limits.

**Observed MCP check:** an MCP JSON-RPC `initialize` exchange succeeded. The server identified itself as `ckan-mcp-server` version `0.4.128` and reported protocol version `2025-03-26`. Tool discovery returned tools for dataset search, package and organization details, DataStore search, and portal discovery. Calls to search and inspect `https://data.gov.ie` returned catalog results and resource metadata. The `ckan_find_portals` call failed with `The 'cache' field on 'RequestInitializerDict' is not implemented`; this is a failure of that tool path, not evidence that CKAN or `data.gov.ie` is generally unavailable.

**Research performed through CKAN**

- Searches for `dual-use`, `strategic goods`, `military exports`, `export licence`, and `export authorisation` returned zero matching datasets in the catalog queries run. A broader `export` search returned 101 records, chiefly general enterprise export statistics. These are query results, not proof that export-control data does not exist in another catalog or form.
- Searches for electricity/energy and research and development returned 55 and 214 results respectively. These are broad contextual-data leads, not case-specific evidence.
- A `complaints Ombudsman` search returned two catalog results, including Fingal County Council complaints and Revenue annual reports; neither establishes anything about the repository's case.
- The Irish State Administration Database (ISAD) package lists four resources. Its organization and event CSV resources have DataStore access; the queried tables reported 914 organization records and 1,165 event records. The fields include organization dates, functions, and source references, and event names, dates, transfers, and source links.
- ISAD event results included entries for S.I. No. 381/2020 and S.I. No. 382/2020, dated 23 and 24 September 2020, describing transfers/replacement involving departments. These are historical leads; the instruments themselves require verification and the records do not establish a specific 2024 handover or operative effect.
- A query of ISAD events for `2024-08-22` returned zero records. This describes that query result only; it does not establish that no event, instrument, or contemporaneous record exists.
- The Department of Justice FOI Decision Logs (July–December 2025) resource reported 2,059 DataStore rows. Only its schema was inspected: reference number, non-personal record description, decision, decision date, and requester type. No individual rows were retrieved for this assessment.

### Repository-to-server functional interface

There is no demonstrated automatic bridge by which these MCP servers ingest, parse, or understand the repository's HTML atom network. The interface exercised here is a research workflow: repository material defines bounded source questions; a caller sends a JSON-RPC tool request to a configured remote endpoint; the server returns external catalog records or metadata; returned source leads are checked against their underlying documents before any repository analysis uses them.

```text
Repository method and source map
  CLAUDE.md + FSD ontology + corpus/index pages + analytical HTML
                         |
                         v
         bounded query / named evidence gap
                         |
                         v
       MCP JSON-RPC tools/call to a server
                         |
                         v
    catalog result, metadata, or source locator
                         |
                         v
      verify the underlying primary document
                         |
                         v
    traceable source -> atom/status -> analysis
```

The layers remain distinct:

| Repository layer / question | Server role in this workflow | What the response can support | What it cannot establish by itself |
|---|---|---|---|
| `corpus/` and `corpus/laws-and-codes/`: locate legislation, instruments, datasets, or institutional records | CKAN locates catalog entries and exposes metadata/DataStore resources. Ansvar could be queried for legal texts after OAuth; that has not happened. | A source lead, catalog description, resource schema, or queryable public table. | That a law was applied, a duty was discharged, a record is complete, or a case-specific event occurred. |
| `semiotics/`: identify terms, framings, oppositions, and intertextual references in repository documents | A query can locate external texts or datasets relevant to a signifier or referenced institution. | Candidate external material to compare with an exact repository passage. | The meaning or significance of a repository signifier; that is an interpretation grounded in text. |
| `behaviour/`: actions, non-actions, delays, referrals, and closures | CKAN may surface organizational histories or public datasets; decision-log metadata may help assess whether a relevant record series exists. | Contextual evidence and possible record locations, subject to source verification. | Receipt, referral, delay, or non-decision in the specific matter unless the underlying records establish it. A search miss is not proof of non-occurrence. |
| `posiwid/`: recurrence, feedback, and system function | Servers can help find counterevidence and additional records; they do not perform the repository's evidentiary synthesis. | Materials that may support or weaken a recurrence hypothesis after review. | System boundaries, recurrence, intent, or POSIWID conclusions from catalog metadata or term frequency alone. |
| `synthesis/`: conclusions and system model | No server role was exercised for generating or validating conclusions. | At most, additional sources for an analyst to test against the existing model. | A substitute for traceable observations, interpretation, counterevidence, or explicit confidence assessment. |

This is a human-directed, source-first connection, not an ETL pipeline or an automated atom importer. Search prompts are discovery instruments; they do not create atoms. Any future ingestion should preserve the source URL/resource, query context, retrieval date, exact passage or record, and evidence status, and must avoid importing generated analytical output as source evidence. In particular, `atoms.json` should not be treated as a direct-observation inventory without tracing its records back to underlying sources.

### Batch design and current coverage

The batch process starts from a repository layer or a documented evidence gap, formulates bounded questions for one server, records the returned source/resource and limitations, then verifies primary sources before moving from discovery to extraction or analysis.

| Batch | Scope and question type | Status |
|---|---|---|
| 1 — Public-data discovery (CKAN) | Search `data.gov.ie` for relevant public datasets, inspect organizations/packages, and inspect selected DataStore schemas or records. | Executed as described above. Search outcomes are scoped to the queries made. |
| 2 — Legal-source verification (Ansvar) | Retrieve exact provisions and citations for legal instruments identified in corpus documents; check scope, version, and dates, then independently verify against official sources. | Not executed: OAuth is required and no authenticated Ansvar MCP session was available. |
| 3 — Competition-law source discovery (Irish Competition) | Establish product scope and locate relevant Irish competition sources before posing substantive queries. | Not executed: configured host did not resolve during checks and authoritative tool documentation remains unverified. |
| 4 — Repository evidence reconciliation | Match returned source leads to source passages in `corpus/`; record supported observations separately from interpretations and hypotheses, and seek counterevidence. | This is the required analyst/repository step; no atoms or analytical files were changed as part of the CKAN discovery batch. |

The ordering is intentional: external MCP results can point to evidence, but the repository's evidence statuses and analytical layers remain governed by `CLAUDE.md` and the source document, not by the server's labels or search ranking.

**Sources**

- Project README: <https://github.com/ondata/ckan-mcp-server>
- Hosted endpoint: <https://ckan-mcp-server.andy-pr.workers.dev/mcp>

### Ansvar Gateway

**Plain language:** A legal and regulatory research connector. Its documentation describes searching legislation, regulations, standards, and threat intelligence, then retrieving exact provisions or decisions with citations.

Ansvar's quickstart says the gateway uses OAuth in a browser, with Dynamic Client Registration and PKCE; an Ansvar account is required, and no API key needs to be pasted into the client configuration. This means the server URL alone is not sufficient to authenticate a new client.

**Observed check:** an unauthenticated GET returned HTTP `401`. No account sign-in, OAuth consent, or MCP initialization request was attempted. The response is consistent with an authentication-protected endpoint, but does not test authenticated availability.

**Sources**

- Ansvar quickstart and setup guide: <https://ansvar.eu/docs>
- Ansvar service site: <https://ansvar.eu>
- Gateway endpoint: <https://gateway.ansvar.eu/mcp>

### Irish Competition

**Plain language (unverified):** the configured name and URL path suggest a service related to Irish competition, but this is not enough to establish which competition-law sources, tools, or functions it provides. Treat this description as a clue from the configuration name, not a verified capability statement.

**Observed check:** the hostname `mcp.ansvar.eu` could not be resolved during the check, so no HTTP response or authentication behavior could be assessed. This may be temporary or environment-specific; it does not prove that the service is permanently unavailable.

**Source**

- Configured endpoint: <https://mcp.ansvar.eu/irish-competition/mcp>

No authoritative product documentation for this endpoint was located during this assessment.

## Credentials and secret handling

- No MCP-specific credential values were present in `.vscode/mcp.json`.
- No CKAN-, Ansvar-, or MCP-named credential environment variables were found in the inspected process environment. Generic GitHub credential variable names were present; their values were not read or disclosed.
- CKAN's hosted project documentation says its endpoint uses no authentication.
- Ansvar's documentation specifies OAuth sign-in rather than a static API key in the JSON file.
- The Irish Competition endpoint's authentication requirements remain unknown.

Do not add access tokens, passwords, or client secrets to this JSON file or commit them to the repository. Use the MCP client’s supported OAuth flow or a credential store intended for secrets.

## Limits and next checks

This assessment records one successful CKAN MCP session and the specific queries/results summarized above. It does **not** establish continuous availability, validate every returned catalog record against its primary source, or connect CKAN results to case-specific events. CKAN's portal-discovery tool returned a compatibility error. Ansvar still needs an authenticated OAuth session before its MCP tools or content can be tested. Irish Competition still needs resolvable DNS and authoritative documentation before its capabilities or authentication can be assessed.

Next checks, if the workflow continues:

1. For each useful CKAN lead, open the underlying dataset and cited source documents; distinguish catalog metadata from source content.
2. Re-query the ISAD event data with organization identifiers, source/instrument names, and date ranges rather than relying on an exact-date text query; verify any returned instruments through official publication sources.
3. Run the legal-source batch only after Ansvar OAuth is completed, or use official public legal sources and label that route distinctly from MCP retrieval.
4. Re-test the Irish Competition endpoint and identify authoritative product documentation before relying on it.
5. Keep repository extraction separate from discovery; do not infer absence, operative effect, recurrence, or an FSD class from catalog search results alone.
