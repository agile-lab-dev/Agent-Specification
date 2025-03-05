# Agent Descriptor Specification

## Overview
This specification defines the attributes of an **autonomous agent** in an agentic system. This specification aims to enable **consistent definition, governance, and observability** of AI-driven agents in a structured format.

## Schema Structure
The agent descriptor follows an **OpenAPI 3.0-based** schema to enable easy documentation and validation.

## Key Attributes

### Identity & Ownership
- `id` *(string, required)* – Unique identifier for the agent. 
- `name` *(string, required)* – Human-readable name of the agent.
- `fullyQualifiedName` *(string)* – Fully qualified name of the agent.
- `description` *(string)* – Describes the agent’s purpose and role.
- `domain` *(string, required)* – The domain in which the agent operates (e.g., trading, security, monitoring).
- `version` *(string, required)* – The version of the agent.
- `environment` *(string)* – Execution environment (development, production, etc.).
- `agentOwner` *(string)* – The primary owner of the agent.
- `agentOwnerDisplayName` *(string)* – Display name of the owner.
- `email` *(string)* – Contact email for support.

### Agent Behavior & Capabilities
- `kind` *(string)* – Type of agent (e.g., decision-making, execution, monitoring).
- `capabilities` *(array)* – List of functionalities the agent supports.
- `executionMode` *(string)* – Mode of execution (e.g., autonomous, event-driven, manual execution).
- `dependencies` *(array)* – Data sources or other agents this agent depends on.

### Observability & Monitoring
- `observability` *(object)* – Includes logs, health checks, and anomaly detection.
  - `healthCheck` – Automated monitoring status.
  - `decisionLogs` – Storage location for decision-making logs.
  - `anomalyDetection` – Indicates whether anomaly detection is enabled.

### Security & Compliance
- `securityInfo` *(object)* – Security and governance attributes.
  - `visibility` – Defines who can see the agent (e.g., Public, Department, Private).
  - `confidentiality` – Classification level (e.g., Confidential, Restricted).
  - `gdpr` *(boolean)* – Indicates whether GDPR compliance is required.

### Domain-Specific Metadata
- `specific` *(object)* – Custom metadata related to the agent, such as model version, optimization frequency, or additional configurations.

## Example Descriptor
```yaml
id: urn:agent:trading:market_strategy:1
name: Market Strategy Agent
fullyQualifiedName: Trading AI Market Strategy Agent
description: Determines trading strategies based on market conditions.
domain: trading
version: 1.2.0
environment: production
agentOwner: john_doe@corp.com
agentOwnerDisplayName: John Doe
email: mailto:trading_team@corp.com
status: ACTIVE
capabilities:
  - DecisionMaking
  - RiskManagement
executionMode: event-driven
dependencies:
  - id: urn:data:market_data
    name: Market Data Feed
    description: Provides real-time market data.
observability:
  healthCheck: Automated monitoring
  decisionLogs: Stored in event database
  anomalyDetection: Enabled
securityInfo:
  visibility: Private
  confidentiality: High
  gdpr: true
specific:
  modelVersion: v2.0
  optimizationFrequency: Daily
```

## How to Use
### 1. Validate Descriptor
Use **OpenAPI tools** to validate the descriptor format.
```sh
yaml-lint agent-descriptor.yaml
```

### 2. Generate Documentation
Convert to **Swagger UI** or **Redoc** format:
```sh
docker run -p 8080:8080 -v $(pwd):/usr/share/nginx/html openapi/swagger-ui
```

### 3. Publish on GitHub
- Add `README.md` and `agent-descriptor.yaml` to a GitHub repository.
- Enable GitHub Pages for automatic documentation generation.

---

For more details, contribute to this repository or submit issues for improvements!
