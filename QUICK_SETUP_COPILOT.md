# 🚀 Quick Setup: Using Your Agent with GitHub Copilot

## Fastest Way to Use Your Agent NOW

While setting up a full GitHub Copilot Extension takes time, here are quick ways to use your agent immediately:

## Option 1: VS Code Task (Recommended - 2 minutes)

This adds your agent as a VS Code task you can run on any HTML file.

### Setup:

1. **In your HTML project**, create `.vscode/tasks.json`:

   ```json
   {
     "version": "2.0.0",
     "tasks": [
       {
         "label": "Convert Headings to Title Case",
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

2. **Use it:**
   - Open any HTML file
   - Press `Ctrl+Shift+P` (or Cmd+Shift+P on Mac)
   - Type "Run Task"
   - Select "Convert Headings to Title Case"
   - Done! ✅

## Option 2: VS Code Keybinding (1 minute)

Add a keyboard shortcut to run your agent.

### Setup:

1. **Open Keyboard Shortcuts:**
   - Press `Ctrl+K Ctrl+S`
   - Or File → Preferences → Keyboard Shortcuts

2. **Search for** "Tasks: Run Task"

3. **Click the + icon** to add keybinding

4. **Press your desired key combo** (e.g., `Ctrl+Alt+T`)

5. **Use it:**
   - Open HTML file
   - Press your key combo
   - Select "Convert Headings to Title Case"

## Option 3: Python Script Integration (30 seconds)

Just run it directly from terminal while working.

### In any HTML project:

```bash
# Single file
python c:/E/Production/Update/title-case/agent/title_case_agent.py index.html

# Multiple files
for file in *.html; do python c:/E/Production/Update/title-case/agent/title_case_agent.py "$file"; done
```

## Option 4: Create a PowerShell Alias (2 minutes)

Make a simple command you can type anywhere.

### Setup:

1. **Edit PowerShell Profile:**

   ```powershell
   notepad $PROFILE
   ```

2. **Add this function:**

   ```powershell
   function Convert-ToTitleCase {
       param([string]$file)
       python c:/E/Production/Update/title-case/agent/title_case_agent.py $file
   }
   Set-Alias titlecase Convert-ToTitleCase
   ```

3. **Reload profile:**

   ```powershell
   . $PROFILE
   ```

4. **Use it:**
   ```powershell
   titlecase myfile.html
   ```

## Option 5: Integrate with GitHub Copilot Chat (5 minutes)

Tell Copilot about your tool in workspace instructions.

### Setup:

1. **In your project root**, create `.github/copilot-instructions.md`:

   ```markdown
   # Project Instructions for GitHub Copilot

   ## HTML Heading Conversion Tool

   This project has a title case converter for HTML headings.

   To convert an HTML file's headings to title case:
   ```

   python c:/E/Production/Update/title-case/agent/title_case_agent.py [filename]

   ```

   This converts <title>, <h1>, <h2>, <h3>, <h4>, <h5> elements to proper title case
   while preserving all attributes and nested elements.

   Example:
   - Input: `<h1>welcome to github copilot</h1>`
   - Output: `<h1>Welcome to Github Copilot</h1>`
   ```

2. **Use with Copilot Chat:**
   - Open Copilot Chat
   - Ask: "Convert the headings in index.html to title case"
   - Copilot will know about your tool and can help you use it!

## Real GitHub Copilot Extension (Full Integration)

For your agent to appear in the `@` dropdown in Copilot Chat, you need to:

1. **Create a web server** to host your agent (see DEPLOYMENT.md)
2. **Create a GitHub App** with Copilot Extension enabled
3. **Deploy the server** (Azure, Heroku, or other hosting)
4. **Configure the GitHub App** with your server URL
5. **Install the GitHub App** to your account
6. **Wait for approval** (if publishing publicly)

**Estimated time:** 2-4 hours for full setup

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete instructions.

## Comparison

| Method               | Setup Time | Use Case                 | Agent in Dropdown? |
| -------------------- | ---------- | ------------------------ | ------------------ |
| VS Code Task         | 2 min      | Personal projects        | No                 |
| Keybinding           | 1 min      | Quick access             | No                 |
| Direct Script        | 30 sec     | One-time use             | No                 |
| PowerShell Alias     | 2 min      | Terminal workflow        | No                 |
| Copilot Instructions | 5 min      | AI-assisted usage        | No                 |
| **Full Extension**   | 2-4 hrs    | **Official integration** | **Yes** ✅         |

## My Recommendation

### For Immediate Use:

**Start with Option 1 (VS Code Task)** - It's fast, integrated, and works great!

### For Long-term:

**Build the Full Extension** (follow DEPLOYMENT.md) - Makes it available to others and integrates seamlessly with Copilot Chat.

## Current Status of Your Agent

✅ **Works locally** - Agent is fully functional  
✅ **Committed to git** - Code is in your GitHub repo  
✅ **Has configuration** - `.github/copilot/agent.json` is ready  
⏸️ **Not yet deployed** - Needs web server + GitHub App setup  
❌ **Not in dropdown** - Requires full GitHub Copilot Extension setup

## Action Plan

**Today (5 minutes):**

1. Set up VS Code Task (Option 1 above)
2. Test it on your HTML files
3. Start using it immediately! ✅

**This Week (2-4 hours):**

1. Read [DEPLOYMENT.md](DEPLOYMENT.md)
2. Deploy web server (Azure/Heroku)
3. Create GitHub App
4. Register as Copilot Extension
5. Install and test
6. Share with others! 🎉

---

**Bottom Line:** Your agent is ready to use locally right now. Setting it up as a full GitHub Copilot Extension (to appear in the dropdown) requires deploying a web server and creating a GitHub App, which takes a few hours.

Start using it locally today with VS Code Tasks, then build the full extension when you have time! 🚀
