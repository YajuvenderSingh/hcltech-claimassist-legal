#!/usr/bin/env python3
"""
DynamoDB Table Setup Script for HCL IDP Solution
Creates hcltech-doc-extraction and hcltech-doc-dashboard tables
"""

import boto3
import json
import sys
from botocore.exceptions import ClientError

def create_dynamodb_table(table_name, key_schema, attribute_definitions, region='us-east-1'):
    """
    Create a DynamoDB table with specified configuration
    """
    dynamodb = boto3.client('dynamodb', region_name=region)
    
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            BillingMode='PAY_PER_REQUEST',
            TableClass='STANDARD',
            DeletionProtectionEnabled=True,
            WarmThroughput={
                'ReadUnitsPerSecond': 12000,
                'WriteUnitsPerSecond': 4000
            }
        )
        
        print(f"✅ Creating table: {table_name}")
        print(f"   Table ARN: {response['TableDescription']['TableArn']}")
        
        # Wait for table to become active
        waiter = dynamodb.get_waiter('table_exists')
        print(f"⏳ Waiting for table {table_name} to become active...")
        waiter.wait(TableName=table_name)
        print(f"✅ Table {table_name} is now active")
        
        return True
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print(f"⚠️  Table {table_name} already exists")
            return True
        else:
            print(f"❌ Error creating table {table_name}: {e}")
            return False

def setup_hcl_tables(region='us-east-1'):
    """
    Set up both HCL tables with the same schema as NMM tables
    """
    print("🚀 Setting up HCL DynamoDB tables...")
    
    # Common table configuration
    key_schema = [
        {
            'AttributeName': 'docid',
            'KeyType': 'HASH'
        }
    ]
    
    attribute_definitions = [
        {
            'AttributeName': 'docid',
            'AttributeType': 'S'
        }
    ]
    
    tables_to_create = [
        'hcltech-doc-extraction',
        'hcltech-doc-dashboard'
    ]
    
    success_count = 0
    
    for table_name in tables_to_create:
        if create_dynamodb_table(table_name, key_schema, attribute_definitions, region):
            success_count += 1
    
    print(f"\n📊 Summary:")
    print(f"   Tables created/verified: {success_count}/{len(tables_to_create)}")
    
    if success_count == len(tables_to_create):
        print("✅ All tables are ready!")
        return True
    else:
        print("❌ Some tables failed to create")
        return False

def verify_tables(region='us-east-1'):
    """
    Verify that tables exist and are active
    """
    dynamodb = boto3.client('dynamodb', region_name=region)
    
    tables_to_check = [
        'hcltech-doc-extraction',
        'hcltech-doc-dashboard'
    ]
    
    print("\n🔍 Verifying tables...")
    
    for table_name in tables_to_check:
        try:
            response = dynamodb.describe_table(TableName=table_name)
            status = response['Table']['TableStatus']
            item_count = response['Table']['ItemCount']
            
            print(f"✅ {table_name}: {status} (Items: {item_count})")
            
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                print(f"❌ {table_name}: NOT FOUND")
            else:
                print(f"❌ {table_name}: ERROR - {e}")

def main():
    """
    Main function to set up HCL tables
    """
    print("=" * 60)
    print("HCL IDP Solution - DynamoDB Table Setup")
    print("=" * 60)
    
    # Get region from command line or use default
    region = sys.argv[1] if len(sys.argv) > 1 else 'us-east-1'
    print(f"🌍 Region: {region}")
    
    # Setup tables
    success = setup_hcl_tables(region)
    
    # Verify tables
    verify_tables(region)
    
    if success:
        print("\n🎉 Setup completed successfully!")
        print("\n📝 Next steps:")
        print("   1. Update your Python code to use the new table names")
        print("   2. Test the application with the new tables")
        print("   3. Configure appropriate IAM permissions")
    else:
        print("\n❌ Setup completed with errors. Please check the logs above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
