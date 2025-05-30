# Port-Scanner-Nmap-lite-alternative-
Explanation:

    socket.socket() – creates a connection object

    connect_ex() – returns 0 if port is open

    getservbyport() – identifies common service (e.g., HTTP, SSH)

    Timeout set to 0.5s for speed

✅ Requirements:

    Pure Python (No extra library)

    Run with python3 port_scanner.py

🔐 Ethical Tip:

Use only on your own systems or with permission. Unauthorized port scanning is illegal on external systems.
