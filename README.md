# HCLTech Legal Agentcore Agent (hcltech-claimassist-legal)

This project implements a multi-agent system for intelligent document processing using AWS Bedrock AgentCore. The system processes legal documents through a sequential workflow of extraction, classification, and entity extraction.

## Architecture Overview

The system consists of three specialized agents coordinated by an orchestrator:

1. **Document Extraction Agent** → 2. **Document Classification Agent** → 3. **Entity Extraction Agent**

## Python Files Description

### Core Agent Files

#### `agent1_docextraction_agent.py`
**Purpose**: Document text extraction from S3 using AWS Textract
- **Main Function**: `doc_extraction(docid, indexid, s3files)`
- **Functionality**:
  - Extracts text and tables from PDF documents stored in S3
  - Uses AWS Textract for OCR and document analysis
  - Stores extracted data in DynamoDB table `nmm-doc-extraction`
  - Handles both synchronous and asynchronous Textract operations
- **Dependencies**: boto3, textract, trp (Textract Response Parser)
- **Output**: Raw text, table data, and key-value pairs stored in database

#### `agent2_docclassification_agent.py`
**Purpose**: Document classification using AI models
- **Main Function**: `get_classification(docid)`
- **Functionality**:
  - Retrieves extracted document data from DynamoDB
  - Uses Bedrock AI models to classify document types
  - Stores classification results back to database
  - Supports various legal document types (contracts, claims, etc.)
- **Dependencies**: boto3, bedrock runtime
- **Input**: Document ID from previous extraction step
- **Output**: Document classification stored in database

#### `agent3_doc_entity_extraction.py`
**Purpose**: Entity extraction based on document classification
- **Main Function**: `extract_entities_based_on_config(docid, classification, s3configfile)`
- **Functionality**:
  - Loads entity extraction configuration from S3
  - Extracts specific entities based on document classification
  - Uses AI models to identify relevant information (dates, amounts, names, etc.)
  - Stores extracted entities in database
- **Dependencies**: boto3, bedrock runtime
- **Input**: Document ID, classification result, S3 config file path
- **Output**: Structured entity data stored in database

### Orchestrator File

#### `orchestrator-agent.py`
**Purpose**: Advanced multi-agent orchestrator (current version)
- **Main Function**: Coordinates all three agents in sequence
- **Functionality**:
  - Implements complete IDP workflow
  - Sequential execution: extraction → classification → entity extraction
  - Uses Claude 3.7 Sonnet model
  - Comprehensive error handling and logging
- **Tools Available**:
  - `doc_extraction_tool`: Wraps agent1 functionality
  - `get_classification_tool`: Wraps agent2 functionality  
  - `get_doc_entity_extraction_tool`: Wraps agent3 functionality
- **Workflow**: Processes documents end-to-end with all three agents

### Deployment and Configuration

#### `agentcore-orchestrator-deployer.py`
**Purpose**: Deployment automation script
- **Functionality**:
  - Automates deployment of agents to AWS Bedrock AgentCore
  - Handles container builds and ECR pushes
  - Manages agent configuration and registration
  - Sets up AWS resources and permissions
- **Usage**: Run to deploy the entire agent system to AWS

#### `.bedrock_agentcore.yaml`
**Purpose**: AgentCore configuration file
- **Contains**:
  - Agent definitions and metadata
  - Deployment configurations (container, runtime settings)
  - AWS resource specifications (IAM roles, ECR repositories)
  - Network and security configurations
- **Default Agent**: `yaju_legal_orchestrator_agent1`

## Configuration Files

#### `requirements.txt`
Python dependencies:
- `strands-agents`: Core agent framework
- `strands-agents-tools`: Additional agent tools
- `boto3`: AWS SDK
- `bedrock-agentcore`: AWS Bedrock AgentCore SDK
- `textract-trp`: Textract response parser
- `uv`: Fast Python package installer

#### `Dockerfile`
Container configuration for agent deployment

#### `.dockerignore`
Files to exclude from Docker build context

## Database Schema

The system uses DynamoDB tables:
- **nmm-doc-extraction**: Stores extracted document text and metadata
- **nmm-doc-dashboard**: Stores document dashboard results  

## Usage Workflow

1. **Document Upload**: Place PDF documents in S3 bucket
2. **Extraction**: Agent1 extracts text using Textract
3. **Classification**: Agent2 classifies document type
4. **Entity Extraction**: Agent3 extracts relevant entities based on classification and configuration file
5. **Results**: All data stored in DynamoDB for downstream processing

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. Configure AWS credentials and permissions
3. Update `.bedrock_agentcore.yaml` with your AWS account details
4. Deploy using: `python agentcore-orchestrator-deployer.py`
5. Run orchestrator: `python orchestrator-agent.py`

## Key Features

- **Sequential Processing**: Agents execute in logical order
- **Error Handling**: Comprehensive error management and logging
- **Scalable**: Container-based deployment on AWS
- **Configurable**: Entity extraction rules via S3 configuration files
- **Multi-format Support**: Handles various document types and formats

## AWS Services Used

- **Bedrock AgentCore**: Agent orchestration and management
- **Textract**: Document text extraction and OCR
- **Bedrock Runtime**: AI model inference
- **DynamoDB**: Data storage and retrieval
- **S3**: Document and configuration file storage
- **ECR**: Container image registry
- **IAM**: Security and permissions management

