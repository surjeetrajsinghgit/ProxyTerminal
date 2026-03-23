# Isolated CMD Proxy Launcher

**The ultimate painkiller for installing Python modules behind a proxy or firewall.**

## 🛑 The Problem
If you have ever tried to run `pip install` on a restricted work network or behind an authenticated proxy, you know it is an awful experience. Dealing with SSL errors, connection timeouts, and manually typing out `http_proxy` variables with URL-encoded passwords every single time you open a terminal is exhausting. 

## 💡 The Solution
This lightweight GUI application instantly spins up an isolated Windows Command Prompt pre-configured with your exact proxy and authentication settings. 

It handles the annoying password URL-encoding automatically in the background and injects the proxy straight into the CMD's local memory. You just open the app, enter your details, click launch, and type `pip install <package>`. It just works.

## ✨ Key Features
* **Painless Pip Installs:** Connects command-line tools like `pip`, `git`, and `npm` seamlessly through your proxy.
* **Automatic Credential Encoding:** Safely processes complex passwords containing special characters (like `@`, `!`, `#`) by automatically URL-encoding them before building the proxy string.
* **Zero System Impact:** Strictly modifies the environment variables of a single, sandboxed CMD window. It makes absolutely zero changes to your Windows Registry or Group Policy, leaving your main OS and web browsers untouched.
* **Portable:** Can be compiled into a single standalone `.exe` file that requires no installation and no administrator privileges.

## 🚀 How to Use It
1. Run the `Proxy_terminal.exe` file.
2. Enter your proxy IP, Port, and your network Username/Password.
3. Click **Launch Proxy Terminal**. 
4. A new black terminal window will open. You can now run `pip install`, `git clone`, or `curl` commands without any connection errors!
