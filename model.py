# generated by datamodel-codegen:
#   filename:  agent-specification.yaml
#   timestamp: 2025-03-21T12:44:27+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Kind(Enum):
    Supervisor = 'Supervisor'
    Single_Agent = 'Single Agent'
    Multi_Agent = 'Multi Agent'
    Router = 'Router'


class TargetUser(Enum):
    internal = 'internal'
    customer = 'customer'


class ValueGeneration(Enum):
    DecisionMaking = 'DecisionMaking'
    Derisking = 'Derisking'
    ProcessAutomation = 'ProcessAutomation'
    InformationRetrieval = 'InformationRetrieval'


class InteractionMode(Enum):
    RequestResponse = 'RequestResponse'
    MultiTurnConversation = 'MultiTurnConversation'
    HumanInTheLoop = 'HumanInTheLoop'


class RunMode(Enum):
    Reactive = 'Reactive'
    Scheduled = 'Scheduled'
    RealTime = 'RealTime'


class AgencyLevel(Enum):
    StaticWorkflow = 'StaticWorkflow'
    ModelDrivenWorkflow = 'ModelDrivenWorkflow'


class LearningCapability(Enum):
    None_ = 'None'
    Reinforcement_Learning = 'Reinforcement Learning'
    Fine_Tuning = 'Fine Tuning'


class Endpoint(BaseModel):
    apiUrl: Optional[str] = Field(
        None,
        description='The primary API URL for interacting with the agent.',
        example='https://api.tradingagent.com/v1',
    )
    authenticationMethod: Optional[str] = Field(
        None, description='Type of authentication required.', example='OAuth2'
    )
    supportedMethods: Optional[List[str]] = Field(
        None,
        description='List of HTTP methods supported.',
        example=['GET', 'POST', 'PUT', 'DELETE'],
    )


class Dependency(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class Audit(BaseModel):
    healthCheck: Optional[str] = Field(
        None,
        description='Automated monitoring endpoint.',
        example='https://api.tradingagent.com/v1/health',
    )
    decisionLogs: Optional[str] = Field(
        None,
        description='Endpoint to retrieve decision logs.',
        example='https://api.tradingagent.com/v1/logs',
    )
    anomalyDetection: Optional[str] = Field(
        None,
        description='API endpoint for anomaly detection.',
        example='https://api.tradingagent.com/v1/anomalies',
    )


class SourceType(Enum):
    Structured = 'Structured'
    Unstructured = 'Unstructured'
    Streaming = 'Streaming'
    Historical = 'Historical'


class KnowledgeBase(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    sourceType: Optional[SourceType] = Field(
        None, description='Type of data source.', example='Structured'
    )
    description: Optional[str] = None
    endpoint: Optional[str] = Field(
        None,
        description='API or database connection string.',
        example='https://datawarehouse.company.com/api',
    )


class SecurityInfo(BaseModel):
    visibility: Optional[str] = Field(None, example='Private')
    confidentiality: Optional[str] = Field(None, example='High')
    gdprSensitive: Optional[bool] = Field(None, example=True)


class Kind1(Enum):
    Tool = 'Tool'
    LLM = 'LLM'
    LocalMemory = 'LocalMemory'
    Guardrail = 'Guardrail'
    Orchestrator = 'Orchestrator'


class AgentComponent(BaseModel):
    id: str = Field(
        ...,
        description='Unique identifier for the component.',
        example='urn:component:my_domain:tool:1',
    )
    name: str = Field(
        ...,
        description='Human-readable name of the component.',
        example='Trade Execution Tool',
    )
    kind: Kind1 = Field(
        ...,
        description='Type of component (e.g., Tool, LLM, LocalMemory, Guardrail, Monitor, Orchestrator).',
        example='Tool',
    )
    version: str = Field(..., description='Version of the component.', example='1.0.0')
    description: Optional[str] = Field(
        None,
        description="Describes the component's purpose and role.",
        example='Executes trades via Interactive Brokers API.',
    )
    dependencies: Optional[List[Dependency]] = Field(
        None,
        description='List of other components or data sources the component depends on.',
    )
    endpoint: Optional[str] = Field(
        None,
        description='MCP endpoint to interact with the component',
        example='https://api.tradingtool.com/v1/execute',
    )
    specific: Optional[Dict[str, Any]] = Field(
        None, description='Additional metadata specific to the component.'
    )


class Tool(AgentComponent):
    inputFormat: Optional[str] = Field(
        None,
        description='Expected input format (e.g., JSON, XML, CSV).',
        example='JSON',
    )
    outputFormat: Optional[str] = Field(
        None, description='Expected output format.', example='JSON'
    )


class LLM(AgentComponent):
    modelName: Optional[str] = Field(
        None, description='The name of the large language model used.', example='GPT-4'
    )
    fineTuned: Optional[bool] = Field(
        None,
        description='Whether the model has been fine-tuned for a specific task.',
        example=True,
    )
    apiProvider: Optional[str] = Field(
        None, description='Provider of the model API.', example='OpenAI'
    )


class LocalMemory(AgentComponent):
    storageType: Optional[str] = Field(
        None,
        description='Type of memory storage (e.g., Redis, SQLite, In-Memory Cache).',
        example='Redis',
    )
    persistence: Optional[bool] = Field(
        None, description='Whether the memory persists across agent runs.', example=True
    )


class EnforcementLevel(Enum):
    Hard = 'Hard'
    Soft = 'Soft'


class Guardrail(AgentComponent):
    enforcementLevel: Optional[EnforcementLevel] = Field(
        None,
        description='Defines whether the rule is strictly enforced or flexible.',
        example='Hard',
    )
    condition: Optional[str] = Field(
        None,
        description='Business condition enforced by the guardrail.',
        example='Prevent trade execution if risk exceeds 5%',
    )
    action: Optional[str] = Field(
        None,
        description='Action taken when the guardrail is triggered (e.g., block, notify, log).',
        example='Block trade',
    )


class Orchestrator(AgentComponent):
    workflowManagement: Optional[str] = Field(
        None,
        description='Defines how the orchestrator manages workflows.',
        example='State-based workflow engine',
    )
    executionOrder: Optional[List[str]] = Field(
        None,
        description='Defines the sequence of components executed.',
        example=['Tool', 'Memory', 'LLM'],
    )


class AgentDescriptor(BaseModel):
    id: str = Field(
        ...,
        description='Unique identifier for the agent.',
        example='urn:agent:finance:trading_agent:1',
    )
    name: str = Field(
        ..., description='Human-readable name of the agent.', example='My Trading Agent'
    )
    fullyQualifiedName: Optional[str] = Field(
        None,
        description='Fully qualified name of the agent.',
        example='My Trading Agent',
    )
    description: Optional[str] = Field(
        None, description='Describes the agent’s purpose and role.'
    )
    domain: str = Field(
        ..., description='The domain in which the agent operates.', example='finance'
    )
    version: str = Field(..., description='The version of the agent.', example='1.0.0')
    environment: Optional[str] = Field(
        None,
        description='Execution environment (e.g., development, production).',
        example='production',
    )
    agentOwner: Optional[str] = Field(
        None, description='The primary owner of the agent.'
    )
    agentOwnerDisplayName: Optional[str] = Field(
        None, description='Display name of the owner.'
    )
    email: Optional[str] = Field(
        None,
        description='Contact email for the agent.',
        example='mailto:support@corp.com',
    )
    status: str = Field(
        ..., description='Deployment status of the agent.', example='ACTIVE'
    )
    kind: Optional[Kind] = Field(
        None,
        description='Agent type to support different agentic system architectures',
        example='Supervisor',
    )
    agentGoal: Optional[str] = Field(
        None,
        description='optimize returns and risk',
        example='Try to keep the balance between a yield return of 10% and a portfolio volatility no more than 3%',
    )
    targetUser: Optional[TargetUser] = Field(
        None, description='The final user of the agent'
    )
    valueGeneration: Optional[ValueGeneration] = Field(
        None,
        description='In which way this Agent generates value for the organization',
        example='Derisking',
    )
    interactionMode: Optional[InteractionMode] = Field(
        None,
        description='Mode of execution (e.g., autonomous, human in the loop).',
        example='Autonoumous',
    )
    runMode: Optional[RunMode] = Field(
        None, description='How the agent execution is triggered', example='Scheduled'
    )
    agencyLevel: Optional[AgencyLevel] = Field(
        None,
        description='How big is the agency for this agent',
        example='Rule Constrained',
    )
    toolsUse: Optional[bool] = Field(
        None,
        description='Define if the system can use tools in order to execute its task',
    )
    learningCapability: Optional[LearningCapability] = Field(
        None,
        description='How the agent will learn on the way',
        example='Reinforcement Learning',
    )
    endpoint: Optional[Endpoint] = Field(
        None,
        description='Defines where external systems or users can communicate with the agent.',
    )
    dependencies: Optional[List[Dependency]] = Field(
        None, description='List of other agents this agent relies on.'
    )
    components: Optional[List[AgentComponent]] = Field(
        None,
        description='Different components that make up the agent, including reasoners, tools, LLMs, and local memory.',
        max_items=100,
    )
    audit: Optional[Audit] = Field(None, description='Monitoring and logging details.')
    knowledgeBases: Optional[List[KnowledgeBase]] = Field(
        None, description='Where this agent reads data from.'
    )
    securityInfo: Optional[SecurityInfo] = Field(
        None, description='Security and compliance details.'
    )
    specific: Optional[Dict[str, Any]] = Field(
        None, description='Any domain-specific metadata related to the agent.'
    )
