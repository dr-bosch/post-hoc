# MCP Server Configuration — Technical Assessment

**Assessment date:** 2026-09-28  
**Configuration assessed:** `.vscode/mcp.json`  
**Purpose:** explain the configured servers in plain language, summarize their authentication and reachability status, and distinguish verified capabilities from assumptions.

## Executive summary

The configuration lists three remote MCP endpoints:

| Configured name | Plain-language description | Authentication / credentials | Connection check |
|---|---|---|---|
| `ckan` | Search public-data portals for datasets, organizations, metadata, and tabular data. | The project describes the hosted endpoint as requiring no authentication. | Responded to a basic unauthenticated HTTP GET with `405`. This shows the host answered, but does not verify an MCP session. |
| `ansvar` | Search legislation, regulations, standards, and related regulatory material; retrieve specific provisions or decisions with citations. | Ansvar's setup documentation describes browser-based OAuth 2.1 sign-in and says no API key needs to be pasted. | Responded to an unauthenticated HTTP GET with `401`, consistent with an endpoint requiring authentication. No OAuth flow or MCP handshake was completed. |
| `irish-competition` | The name suggests an Irish competition-law service, but its actual scope and tools could not be verified from an authoritative source during this assessment. | Not verified. The JSON contains no credential configuration. | DNS lookup for `mcp.ansvar.eu` failed during the check; the endpoint was not reached. |

These are configuration entries, not proof that any server is currently connected to this Copilot CLI session. A basic GET probe is also not an MCP protocol handshake. The checks did not send credentials.

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

**Observed check:** an unauthenticated GET to the MCP URL returned HTTP `405`. A `405` response means the server did not accept that HTTP method at that endpoint; it does not establish whether a valid MCP client request would succeed.

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

This assessment records the configuration and a basic reachability probe. It does **not** confirm a successful MCP `initialize` exchange, enumerate tools, validate returned data, or establish that the services are currently connected in Copilot CLI. A full check would require the relevant MCP client to load the configuration and, for Ansvar, complete OAuth authentication. The Irish Competition service needs resolvable DNS and authoritative documentation before its capabilities or authentication can be assessed.
