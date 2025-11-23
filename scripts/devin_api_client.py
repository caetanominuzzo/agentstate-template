#!/usr/bin/env python3
"""Shared Devin API HTTP client."""
import argparse
import json
import os
import sys
import requests


class DevinAPIClient:
    """Client for Devin API interactions."""
    
    def __init__(self):
        self.api_token = os.environ.get('DEVIN_API')
        if not self.api_token:
            print('{"error": "DEVIN_API environment variable not set"}', file=sys.stderr)
            sys.exit(1)
        
        self.base_url = "https://api.devin.ai/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
    
    def spawn_session(self, repo, task, context=None):
        """Spawn a new Devin session."""
        payload = {
            "repo": repo,
            "task": task
        }
        if context:
            payload["context"] = context
        
        try:
            response = requests.post(
                f"{self.base_url}/sessions",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(json.dumps({"error": str(e)}), file=sys.stderr)
            sys.exit(1)
    
    def get_session(self, session_id):
        """Get session status."""
        try:
            response = requests.get(
                f"{self.base_url}/sessions/{session_id}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(json.dumps({"error": str(e)}), file=sys.stderr)
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='Devin API Client')
    parser.add_argument('action', choices=['spawn', 'status'], help='Action to perform')
    parser.add_argument('--repo', help='Repository name')
    parser.add_argument('--task', help='Task description')
    parser.add_argument('--context', help='Context JSON string')
    parser.add_argument('--session-id', help='Session ID for status check')
    
    args = parser.parse_args()
    
    client = DevinAPIClient()
    
    if args.action == 'spawn':
        if not args.repo or not args.task:
            print('{"error": "repo and task are required for spawn"}', file=sys.stderr)
            sys.exit(1)
        
        context = json.loads(args.context) if args.context else None
        result = client.spawn_session(args.repo, args.task, context)
        print(json.dumps(result, indent=2))
    
    elif args.action == 'status':
        if not args.session_id:
            print('{"error": "session-id is required for status"}', file=sys.stderr)
            sys.exit(1)
        
        result = client.get_session(args.session_id)
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

