# HCLTech Intelligent Document Processing (IDP) Solution

[![AWS](https://img.shields.io/badge/AWS-Bedrock%20AgentCore-orange)](https://aws.amazon.com/bedrock/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-Commercial-green)](LICENSE)

## Overview

HCLTech's Intelligent Document Processing (IDP) Solution is an enterprise-grade, AI-powered document processing system built on AWS Bedrock AgentCore. This solution automates the extraction, classification, and entity recognition from legal and business documents using a sophisticated multi-agent architecture.

### Key Benefits

- **🚀 Automated Processing**: End-to-end document processing with minimal human intervention
- **🎯 High Accuracy**: Advanced AI models ensure precise document classification and entity extraction
- **⚡ Scalable Architecture**: Container-based deployment scales automatically with your workload
- **🔒 Enterprise Security**: Built on AWS with comprehensive security and compliance features
- **📊 Real-time Insights**: Immediate processing results stored in DynamoDB for instant access

## Solution Architecture

The solution employs a sequential multi-agent workflow:

```
Document Upload → Agent 1 (Extraction) → Agent 2 (Classification) → Agent 3 (Entity Extraction) → Results
```

### Agent Workflow

1. **Document Extraction Agent**: Extracts text, tables, and key-value pairs using AWS Textract
2. **Document Classification Agent**: Classifies documents into predefined categories using AI models
3. **Entity Extraction Agent**: Extracts specific entities based on document classification
4. **Orchestrator Agent**: Coordinates the entire workflow and manages agent interactions

## Features

### Core Capabilities

- **Multi-format Document Support**: PDF, images, and scanned documents
- **Advanced OCR**: AWS Textract integration for high-accuracy text extraction
- **Intelligent Classification**: AI-powered document type identification
- **Configurable Entity Extraction**: Customizable entity recognition rules
- **Real-time Processing**: Immediate results with comprehensive logging
- **Error Handling**: Robust error management and recovery mechanisms

### Technical Features

- **Container-based Deployment**: Docker containers for consistent deployment
- **AWS Native Integration**: Seamless integration with AWS services
- **Scalable Storage**: DynamoDB for high-performance data storage
- **Monitoring & Observability**: Built-in logging and monitoring capabilities
- **Security**: IAM-based access control and encryption at rest

## Quick Start

### Prerequisites

- AWS Account with appropriate permissions
- SageMaker Studio or Jupyter environment
- IAM roles configured for Bedrock AgentCore
- Access to AWS services: DynamoDB, Textract, Bedrock, S3

### Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd legal-idp-agents
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Resources**
   - Update `.bedrock_agentcore.yaml` with your AWS account details
   - Ensure proper IAM permissions are configured

4. **Run the Setup Guide**
   Open and execute `HCLTech_IDP_Setup_Guide.ipynb` in your Jupyter environment. This notebook provides:
   - Step-by-step setup instructions
   - Database table creation
   - Agent deployment
   - Testing procedures

### Deployment

The solution can be deployed using the provided setup guide:

```bash
# Follow the HCLTech_IDP_Setup_Guide.ipynb notebook for complete deployment
```

**Estimated Setup Time**: 45-60 minutes
- Database Setup: 5 minutes
- Agent Configuration: 15 minutes
- Deployment: 20-30 minutes
- Testing: 5-10 minutes

## Usage

### Document Processing Workflow

1. **Upload Documents**: Place PDF documents in the configured S3 bucket
2. **Initiate Processing**: Call the orchestrator agent with document details
3. **Monitor Progress**: Track processing status through CloudWatch logs
4. **Retrieve Results**: Access processed data from DynamoDB tables

### API Integration

The solution exposes RESTful APIs through AWS Bedrock AgentCore:

```python
# Example usage
response = orchestrator_agent.invoke({
    "docid": "DOC123456",
    "indexid": "IDX789",
    "s3files": "bucket/path/to/document.pdf"
})
```

## Configuration

### Environment Variables

- `AWS_REGION`: AWS region for deployment (default: us-east-1)
- `AWS_DEFAULT_REGION`: Default AWS region
- `DOCKER_CONTAINER`: Container environment flag

### Database Tables

The solution creates and manages the following DynamoDB tables:
- `hcltech-doc-extraction`: Stores extracted document content
- `hcltech-doc-classification`: Stores document classification results
- `hcltech-doc-entities`: Stores extracted entity information

### Customization

Entity extraction rules can be customized by modifying configuration files stored in S3. The system supports:
- Custom entity types
- Industry-specific extraction rules
- Configurable confidence thresholds
- Custom classification categories

## AWS Services Integration

### Core Services

- **AWS Bedrock AgentCore**: Agent orchestration and management
- **AWS Textract**: Document text extraction and OCR
- **AWS Bedrock**: AI model inference for classification and entity extraction
- **Amazon DynamoDB**: High-performance data storage
- **Amazon S3**: Document and configuration storage

### Supporting Services

- **Amazon ECR**: Container image registry
- **AWS IAM**: Security and access management
- **Amazon CloudWatch**: Monitoring and logging
- **AWS CodeBuild**: Automated container builds

## Performance & Scalability

- **Processing Speed**: Handles documents in seconds to minutes depending on complexity
- **Throughput**: Scales automatically based on demand
- **Availability**: 99.9% uptime with AWS infrastructure
- **Storage**: Unlimited document storage capacity with S3

## Security & Compliance

- **Data Encryption**: Encryption at rest and in transit
- **Access Control**: IAM-based fine-grained permissions
- **Audit Logging**: Comprehensive audit trails
- **Compliance**: Supports SOC, HIPAA, and other compliance frameworks
- **Network Security**: VPC isolation and security groups

## Support & Documentation

### Getting Started
- Complete setup guide: `HCLTech_IDP_Setup_Guide.ipynb`
- API documentation included in agent files
- Configuration examples provided

### Troubleshooting
- Comprehensive error handling and logging
- CloudWatch integration for monitoring
- Detailed error messages and recovery procedures

### Professional Support
For enterprise support, customization, and professional services, contact HCLTech.

## Pricing

This solution leverages AWS pay-as-you-use pricing model:
- **Compute**: Bedrock AgentCore runtime costs
- **Storage**: DynamoDB and S3 storage costs
- **AI Services**: Bedrock model inference costs
- **Document Processing**: Textract processing costs

Use the [AWS Pricing Calculator](https://calculator.aws) for detailed cost estimates.

## License

This solution is provided under a commercial license. See LICENSE file for details.

## About HCLTech

HCLTech is a global technology company that helps enterprises reimagine their businesses for the digital age. Our technology products, services, and engineering are built on four decades of innovation, with a world-renowned management philosophy, a strong culture of invention and risk-taking, and a relentless focus on customer relationships.

---

**Ready to transform your document processing workflow?** Deploy the HCLTech IDP Solution today and experience the power of AI-driven document intelligence.

For technical support or questions, please refer to the `HCLTech_IDP_Setup_Guide.ipynb` notebook for comprehensive setup and usage instructions.
