# 🚀 Deploying Your Title Case Agent to GitHub Copilot

## Overview

To make your Title Case Agent appear in the GitHub Copilot agent dropdown menu, you need to create and configure it as a **GitHub Copilot Extension** (GitHub App).

## Prerequisites

- ✅ Code committed to GitHub repository
- ✅ GitHub account with access to GitHub Copilot
- ✅ Repository is public or accessible to your GitHub organization
- ✅ Agent code is working locally

## Deployment Options

### Option 1: GitHub Copilot Extension (Recommended)

This makes your agent available in the `@` mention dropdown in GitHub Copilot Chat.

#### Step 1: Create a GitHub App

1. **Go to GitHub Settings:**
   - Navigate to https://github.com/settings/apps
   - Click **"New GitHub App"**

2. **Configure Basic Information:**

   ```
   GitHub App name: Title Case Agent
   Homepage URL: https://github.com/arulkkumar1/title-case
   Webhook URL: (Your server endpoint - see below)
   ```

3. **Set Permissions:**
   - Repository permissions:
     - Contents: Read (to access files)
     - Pull requests: Read & write (optional, for suggestions)

4. **Subscribe to Events:**
   - Check the events your app needs to respond to

#### Step 2: Create a Web Server for Your Agent

Your agent needs a web endpoint to respond to GitHub Copilot requests.

Create `server/app.py`:

```python
from flask import Flask, request, jsonify
from agent.title_case_agent import TitleCaseConverter
import os

app = Flask(__name__)
converter = TitleCaseConverter()

@app.route('/agent', methods=['POST'])
def agent_endpoint():
    """Handle requests from GitHub Copilot"""
    data = request.json

    # Extract the request from GitHub Copilot
    user_message = data.get('message', '')
    file_content = data.get('file_content', '')

    # Process the request
    if 'convert' in user_message.lower() or 'title case' in user_message.lower():
        try:
            result = converter.convert_html(file_content)
            return jsonify({
                'response': result,
                'status': 'success'
            })
        except Exception as e:
            return jsonify({
                'response': f'Error: {str(e)}',
                'status': 'error'
            })

    return jsonify({
        'response': 'I can convert HTML headings to title case. Send me HTML content!',
        'status': 'info'
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

Add to `requirements.txt`:

```
flask>=2.0.0
gunicorn>=20.1.0
```

#### Step 3: Deploy Your Server

**Option A: Deploy to Azure (Recommended for production)**

```bash
# Install Azure CLI
# Then deploy:
az webapp up --name title-case-agent --runtime PYTHON:3.12
```

**Option B: Deploy to Heroku**

```bash
# Install Heroku CLI, then:
heroku create title-case-agent
git push heroku main
```

**Option C: Deploy to GitHub Codespaces**

- Configure port forwarding in your Codespace
- Use the public URL as your webhook URL

#### Step 4: Update Agent Configuration

Update `.github/copilot/agent.json`:

```json
{
  "name": "title-case",
  "version": "1.0.0",
  "description": "Converts HTML heading elements to title case",
  "author": "arulkkumar1",
  "license": "MIT",
  "agent_type": "extension",
  "endpoint": {
    "url": "https://your-server-url.com/agent",
    "method": "POST",
    "headers": {
      "Content-Type": "application/json"
    }
  },
  "capabilities": {
    "chat": true,
    "supportedFileTypes": ["html", "htm"],
    "commands": [
      {
        "name": "convert-to-title-case",
        "description": "Convert all heading elements to title case",
        "usage": "@title-case convert this HTML file"
      }
    ]
  },
  "authentication": {
    "type": "github_app",
    "required": true
  }
}
```

#### Step 5: Register Your Extension with GitHub

1. **In your GitHub App settings:**
   - Go to https://github.com/settings/apps/[your-app-name]
   - Enable **GitHub Copilot Extension**
   - Set the agent endpoint URL

2. **Configure Copilot Integration:**
   - Under "GitHub Copilot" section
   - Add your agent endpoint
   - Set authentication credentials

#### Step 6: Install Your GitHub App

1. **Install to your account:**
   - Go to your GitHub App page
   - Click **"Install App"**
   - Select your account or organization
   - Choose repositories (or all repositories)

#### Step 7: Enable in VS Code

1. **Open VS Code**
2. **Open GitHub Copilot Chat** (Ctrl+Shift+I or Cmd+Shift+I)
3. **Type `@` to see available agents**
4. Your **"title-case"** agent should now appear!

### Option 2: VS Code Extension (Local Agent)

For a local-only agent that works within VS Code workspace:

#### Step 1: Create VS Code Extension

Create `extension/package.json`:

```json
{
  "name": "title-case-agent",
  "displayName": "Title Case Agent",
  "description": "Convert HTML headings to title case",
  "version": "1.0.0",
  "engines": {
    "vscode": "^1.80.0"
  },
  "categories": ["Other"],
  "activationEvents": ["onCommand:title-case.convert"],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "title-case.convert",
        "title": "Convert Headings to Title Case"
      }
    ],
    "configuration": {
      "title": "Title Case Agent",
      "properties": {
        "titleCaseAgent.pythonPath": {
          "type": "string",
          "default": "python",
          "description": "Path to Python executable"
        }
      }
    }
  }
}
```

#### Step 2: Package and Install

```bash
# Install vsce (VS Code Extension CLI)
npm install -g @vscode/vsce

# Package the extension
vsce package

# Install in VS Code
code --install-extension title-case-agent-1.0.0.vsix
```

## Option 3: Simple Workspace Integration (Quickest)

For immediate use without full deployment:

### Method A: Task Integration

Create `.vscode/tasks.json` in your HTML project:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Convert to Title Case",
      "type": "shell",
      "command": "python",
      "args": [
        "c:/E/Production/Update/title-case/agent/title_case_agent.py",
        "${file}"
      ],
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "problemMatcher": []
    }
  ]
}
```

**Usage:** Terminal → Run Task → "Convert to Title Case"

### Method B: Custom Prompt/Instructions

Add to your workspace `.vscode/settings.json`:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": "**/*.html",
      "instruction": "When working with HTML files, you can convert headings to title case by running: python c:/E/Production/Update/title-case/agent/title_case_agent.py [filename]"
    }
  ]
}
```

## Verification Steps

After deployment, verify your agent is working:

1. **Check GitHub App Installation:**

   ```bash
   curl https://api.github.com/users/arulkkumar1/installations
   ```

2. **Test Agent Endpoint:**

   ```bash
   curl -X POST https://your-server-url.com/agent \
     -H "Content-Type: application/json" \
     -d '{"message":"convert","file_content":"<h1>test</h1>"}'
   ```

3. **Test in VS Code:**
   - Open GitHub Copilot Chat
   - Type `@title-case` - should show in dropdown
   - Try: `@title-case convert this file`

## Troubleshooting

### Agent Not Appearing in Dropdown

1. **Check GitHub App is installed:**
   - Visit: https://github.com/settings/installations
   - Verify "Title Case Agent" is listed and enabled

2. **Verify Copilot Extension is enabled:**
   - In GitHub App settings
   - Check "GitHub Copilot Extension" is turned on

3. **Restart VS Code:**
   - Reload window: Ctrl+Shift+P → "Reload Window"

4. **Check VS Code Settings:**
   - Settings → GitHub Copilot
   - Ensure extensions are enabled

### Server Issues

1. **Check server is running:**

   ```bash
   curl https://your-server-url.com/health
   ```

2. **Check logs:**
   - Azure: `az webapp log tail`
   - Heroku: `heroku logs --tail`

3. **Verify webhook URL in GitHub App settings**

## Cost Considerations

- **GitHub App:** Free to create and host
- **Server Hosting:**
  - Azure: ~$10-50/month (App Service)
  - Heroku: Free tier available, then $7/month
  - GitHub Codespaces: Free tier available
  - Self-hosted: Free (use ngrok for testing)

## Next Steps

1. **Choose your deployment option** (Option 1 for full GitHub integration)
2. **Set up the server/endpoint** (if using Option 1)
3. **Create GitHub App** and configure it
4. **Install and test** in VS Code
5. **Share with others** (marketplace or private distribution)

## Need Help?

- GitHub Copilot Extensions Docs: https://docs.github.com/copilot/building-copilot-extensions
- GitHub Apps Guide: https://docs.github.com/apps
- VS Code Extension Guide: https://code.visualstudio.com/api

---

**Note:** The full GitHub Copilot Extension requires a web server to handle requests. For now, you can use the Task Integration (Option 3) for immediate local use while you set up the full extension infrastructure.
