# Agent Descriptor Specification

## Overview
This specification defines the attributes of an **autonomous agent** in an agentic system. This specification aims to enable **consistent definition, governance, and observability** of AI-driven agents in a structured format.

## Schema Structure
The agent descriptor follows an **OpenAPI 3.0-based** schema to enable easy documentation and validation.

## Key Attributes

### **Identity & Ownership**
- `id` *(string, required)* – Unique identifier for the agent.
- `name` *(string, required)* – Human-readable name of the agent.
- `fullyQualifiedName` *(string)* – Fully qualified name of the agent.
- `description` *(string)* – Describes the agent’s purpose and role.
- `domain` *(string, required)* – The domain in which the agent operates (e.g., trading, security, monitoring).
- `version` *(string, required)* – The version of the agent.
- `environment` *(string)* – Execution environment (development, production, etc.).
- `agentOwner` *(string)* – The primary owner of the agent.

### **Business Context & Goals**
- `agentGoal` *(string)* – The primary goal the agent supports.
- `valueGeneration` *(array)* – How this agent generates business value (DecisionMaking, Derisking, ProcessAutomation).
- `executionMode` *(string)* – Defines how the agent operates (Autonomous, Human in the Loop).
- `decisionFrequency` *(string)* – How often the agent makes decisions (Reactive, Scheduled, RealTime).
- `agencyLevel` *(string)* – Defines the autonomy level of the agent (Total, Rule Constrained, Workflow Constrained).
- `learningCapability` *(string)* – Learning approach (None, Reinforcement Learning, Fine Tuning).

### **Technical Configuration**
- `physicalEndpoint` *(object)* – Defines where and how external systems interact with the agent.
  - `apiUrl` *(string)* – API endpoint for agent interaction.
  - `authenticationMethod` *(string)* – Authentication method required (OAuth2, API Key, etc.).
  - `supportedMethods` *(array)* – Supported HTTP methods (GET, POST, PUT, DELETE).

### **Dependencies & Components**
- `dependencies` *(array)* – Other agents or services this agent depends on.
- `components` *(array)* – Different modules within the agent, such as Reasoners, Tools, LLMs, Memory, and Guardrails.

### **Audit & Observability**
- `audit` *(object)* – Monitoring and logging details.
  - `healthCheck` *(string)* – API endpoint for health status.
  - `decisionLogs` *(string)* – API endpoint for retrieving decision logs.
  - `anomalyDetection` *(string)* – API endpoint for anomaly monitoring.

### **Knowledge Bases**
- `knowledgeBases` *(array)* – Data sources the agent uses.
  - `sourceType` *(string)* – Defines if the data source is Structured, Unstructured, Streaming, or Historical.
  - `endpoint` *(string)* – API or database connection for the knowledge base.

### **Security & Compliance**
- `securityInfo` *(object)* – Security details including data visibility, confidentiality, and GDPR compliance.

## Example Agent Descriptor

```yaml
id: urn:agent:finance:trading_agent:1
name: Market Strategy Trading Agent
fullyQualifiedName: AI Trading Market Strategy Agent
description: Determines trading strategies based on market conditions.
domain: finance
version: 1.2.0
environment: production
agentOwner: john_doe@corp.com
agentOwnerDisplayName: John Doe
email: mailto:trading_team@corp.com
status: ACTIVE

agentGoal: "Optimize returns while managing portfolio risk."
valueGeneration: ["DecisionMaking", "Derisking"]
executionMode: "Autonomous"
decisionFrequency: "RealTime"
agencyLevel: "Rule Constrained"
learningCapability: "Reinforcement Learning"

physicalEndpoint:
  apiUrl: "https://api.tradingagent.com/v1"
  authenticationMethod: "OAuth2"
  supportedMethods: ["GET", "POST"]

dependencies:
  - id: urn:data:market_data
    name: Market Data Feed
    description: Provides real-time market data.

components:
  - id: urn:component:finance:market_reasoner:1
    name: Market Strategy Reasoner
    kind: Reasoner
    version: 1.0.0
    description: AI-driven module analyzing trading strategies.
  - id: urn:component:finance:trade_execution_tool:1
    name: Trade Execution Tool
    kind: Tool
    version: 1.2.0
    description: Executes stock trades via Interactive Brokers API.

audit:
  healthCheck: "https://api.tradingagent.com/v1/health"
  decisionLogs: "https://api.tradingagent.com/v1/logs"
  anomalyDetection: "https://api.tradingagent.com/v1/anomalies"

knowledgeBases:
  - id: urn:kb:finance:historical_trades
    name: Historical Trade Database
    sourceType: "Structured"
    description: Stores past trade data for analysis.
    endpoint: "https://datawarehouse.company.com/api"

securityInfo:
  visibility: "Private"
  confidentiality: "High"
  gdprSensitive: true
```


# Agent Component Specification

## Overview
This specification defines the attributes of different **agent components** that can be used within an **agentic system**. These components allow for modular, reusable structures that enable the agent to interact with data, execute actions, and enforce policies.

## Component Types
The following component types are defined:

### **1️⃣ Tool**
A **Tool** is an external service or function that the agent interacts with. It executes commands, fetches data, or performs transformations.

**Key Attributes:**
- API-based execution.
- Well-defined input/output formats.
- May interact with external systems (e.g., stock exchanges, databases, or analytics services).

```yaml
id: urn:component:finance:trade_execution_tool:1
name: Trade Execution Tool
kind: Tool
version: 1.2.0
description: Executes stock trades via Interactive Brokers API.
apiEndpoint: "https://api.tradingtool.com/v1/execute"
inputFormat: "JSON"
outputFormat: "JSON"
```

---

### **2️⃣ LLM (Large Language Model)**
An **LLM** is an AI-driven model that provides natural language understanding, reasoning, or generation capabilities.

**Key Attributes:**
- Utilizes models like **GPT-4, Claude, Gemini, Llama**.
- May be **fine-tuned** for domain-specific knowledge.
- Provides an **API endpoint** for interaction.

```yaml
id: urn:component:nlp:sentiment_analyzer:1
name: Sentiment Analysis LLM
kind: LLM
version: 2.0.0
description: Analyzes market sentiment from news articles.
modelName: "GPT-4"
fineTuned: true
apiProvider: "OpenAI"
```

---

### **3️⃣ Local Memory**
A **Local Memory** component stores **temporary or long-term data** for agent reasoning and contextual awareness.

**Key Attributes:**
- Can be **ephemeral (in-memory)** or **persistent (Redis, SQLite, etc.)**.
- Used for **context retention and decision-making**.

```yaml
id: urn:component:memory:session_cache:1
name: Session Memory Cache
kind: Memory
version: 1.0.0
description: Stores temporary trading session data.
storageType: "Redis"
persistence: false
```

---

### **4️⃣ Guardrail**
A **Guardrail** is a governance mechanism that **enforces constraints on the agent’s decisions**.

**Key Attributes:**
- Defines strict or flexible policies.
- Supports **logging, blocking, or escalating violations**.
- Ensures regulatory compliance (e.g., **GDPR, financial risk limits**).

```yaml
id: urn:component:compliance:trading_guardrail:1
name: Risk Limit Guardrail
kind: Guardrail
version: 1.1.0
description: Prevents trades exceeding 5% of portfolio value.
enforcementLevel: "Hard"
condition: "Prevent trade execution if risk exceeds 5%"
action: "Block trade"
```

---

### **5️⃣ Monitor**
A **Monitor** observes the agent’s performance, logs events, and detects anomalies.

**Key Attributes:**
- Tracks **latency, error rates, anomalies**.
- Sends **alerts when predefined thresholds are exceeded**.

```yaml
id: urn:component:monitoring:latency_monitor:1
name: Latency Performance Monitor
kind: Monitor
version: 1.0.0
description: Monitors latency for trade execution requests.
metricsTracked: ["Latency", "Error Rate"]
monitoringEndpoint: "https://monitoring.company.com/api"
```

---

### **6️⃣ Orchestrator**
An **Orchestrator** manages workflows, ensuring components execute in the correct sequence.

**Key Attributes:**
- Defines **execution order**.
- Ensures dependencies are resolved before execution.

```yaml
id: urn:component:workflow:orchestrator:1
name: Workflow Orchestrator
kind: Orchestrator
version: 1.3.0
description: Controls the execution order of agent components.
workflowManagement: "State-based workflow engine"
executionOrder: ["Tool", "Memory", "LLM"]
```


---

For improvements, open an issue or submit a pull request. 🚀
