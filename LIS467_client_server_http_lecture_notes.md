# LIS 467 — Client/Server Architecture & HTTP

**Course:** LIS 467
**Topic:** Client and Server, HTTP, Addressing on the Internet
**Source:** Lecture video transcript (~18 min)

---

## Learning Objectives

By the end of this lecture you should be able to:

1. Distinguish between a **client** and a **server**
2. Get introduced to **HTTP** (Hypertext Transfer Protocol)
3. Follow the key developments in the history of the internet and the World Wide Web (via Moodle resources and recommended videos)

💡 **Context:** In 2019 the World Wide Web completed 30 years.

---

## 1. What Are Clients and Servers?

⭐ **Core idea:** A **server** is any system that *provides a service*; **clients** are the many systems that *connect to it to request that service*.

| Analogy | Server | Clients |
|---|---|---|
| Library reference desk | The reference librarian at the desk | The many patrons who come to the desk |
| Airline ticket website | The computers "beyond the cloud" running the booking site | The individual laptops, desktops, phones, and tablets connecting to buy tickets |

- The server is not a person but a **computer-based system** providing a service.
- Many client computers connect to one server (often through a local area network or internet connectivity of any size).

🔑 **Things to understand in this unit:**
- Major components of computerized information systems
- **Client-side technologies** — interfaces, input/output, how data is sent from client to server
- **Server-side technologies** — input/output; print server, data server, web server, and other kinds of servers
- The **flow of data**: client → server → back to client

---

## 2. Architecture Tiers

There are many ways of linking a computer to peripherals and other computers: **standalone**, **peer-to-peer**, and additions of the **cloud**.

| Architecture | Description | Example |
|---|---|---|
| **Two-tier** (= client/server architecture) | Presentation layer/interface runs on the *client*; data layer/data storage sits on the *server*. Separating client from server = two-tier. | A client computer connected to a printer and a database server |
| **Three-tier** | Two machines on the server side: an **application server** + a **database server** | Common in larger organizations, where functions are physically separated onto larger machines |
| **N-tier / multi-tier** | One or more clients connect to *multiple* specialized servers — the server work is divided across different machines | Application server + database management server + web server, etc. |

⚠️ **Note:** In a three-tier setup, the application and database servers *can* physically run on the same machine — but larger organizations typically separate them.

💡 **Fun facts from lecture:**
- The stacked-discs symbol (🗄️) in diagrams represents a **database system** — Oracle's headquarters buildings are designed to look like it. Oracle is a major database company.
- **Apache** is a very commonly known web server.
- **Cloud** examples: Dropbox, Google Drive — cloud-based servers that continuously sync data between client and server.

---

## 3. The Request–Response Cycle

⭐ **The end user (you or me at a computer) is the client.**

1. **Client sends data to the server** → this is a **request**
   - Done using **web forms** (e.g., the Gmail login page at www.gmail.com is a web form)
   - Client-side technologies: **HTML and CSS**
2. **Server receives the request and returns a response**
   - Response may be: web pages, data from databases, files — or the server may *pass the request on to another server*

### HTTP Request Methods (Commands)

| Method | Purpose | Example |
|---|---|---|
| **GET** | Client *requests a resource* from the web server | Requesting a web page |
| **POST** | Client *sends information/data* to the server (larger, complex data) | Filling out an online form; submitting username + password |
| Others | HEAD, PUT, DELETE, TRACE, OPTIONS, etc. | Less commonly used |

✅ **Gmail example (walkthrough of the full cycle):**
1. You enter username + password → sent to server via **POST**
2. What you're requesting (your emails) → a **GET**
3. Server accesses your email from the database
4. Server generates HTML, CSS, JavaScript
5. **Response** returned = the list of emails you see in your inbox
6. If your password is wrong, the server may respond **Unauthorized**; a successful request gets an **OK**

### Packets and HTTPS

- All internet communication is sent as **data packets**, each with a **header** and a **body**.
- ⚠️ With plain **HTTP**, packets can be read in transit — piecing packets together is how **data leaks** happen.
- ✅ **HTTPS** = secure HTTP: packets are **encrypted** between client and server, so intercepted packets are useless to an attacker. Most websites now adopt HTTPS.

💡 **Try it yourself (demo from lecture):** In Chrome, visit any site (e.g., simmons.edu) → More Tools → **Developer Tools**. You can see cookies, load times for page elements, and in the Console/Network activity the stream of **GET** and **POST** commands issued as the page loads (including ad requests).

---

## 4. Addressing: MAC, IP, and DNS

### MAC Address (Physical Address)

- Every network device has a unique identifier: the **MAC address** (physical address)
- Format: **hexadecimal** (digits 0–9 and a–f — a base-16 number system), groups separated by colons (e.g., `a0:d3:c1:71:ef:85`)
- 🔑 It is **fixed** — like a name, it doesn't change for a given device
- View it on Windows: Command Prompt → `ipconfig /all` → "Physical Address"

💡 **Simmons Wi-Fi example:** You log in once; your device's MAC address is stored on the Simmons server, so subsequent connections are authorized automatically by MAC address.

### IP Address

- Every time you use the internet, your **Internet Service Provider (ISP)** (e.g., Verizon) assigns your device an **IP address** so servers can locate you
- Typically generated on the fly via **DHCP** (dynamically created addresses)
- 🔑 The IP address uniquely distinguishes computers connected to the internet

| Version | Format | Capacity |
|---|---|---|
| **IPv4** | Four parts ("octets") separated by dots, e.g., `192.168.0.10` or `134.140.12.61` (= simmons.edu) | 2³² addresses — **no longer enough** for all the world's devices |
| **IPv6** | Much longer, hexadecimal addressing | Supports an almost unlimited number of addresses |

### Domain Name Server (DNS)

- Humans use easy-to-remember names (google.com, simmons.edu); computers use numeric IP addresses
- The **domain name server** maps names → IP addresses
- Example: your Simmons computer wants www.bpl.org (Boston Public Library) → the Simmons server asks a domain name server to map `www.bpl.org` to its IP address — you never need to remember the number

### Anatomy of a URL

```
http://www.domain.com:1234/path/to/page?query=value
```

| Part | Meaning |
|---|---|
| `http://` | **Protocol** (could also be HTTPS, FTP/SFTP, SMTP, etc.) |
| `www.domain.com` | **Host name** — the name/address of the server |
| `:1234` | **Port** used to connect to the server |
| `/path/to/page` | **Path/directories** on the server leading to a specific page |
| `?query=value` | **Query** sent to the server, listed after a question mark |

⚠️ HTTP is the most commonly used protocol for exchanging web pages, but others exist: **HTTPS** (secure), **FTP / secure FTP** (file transfer), **SMTP** (simple mail transfer).

---

## 5. Summary

- ⭐ **Client-server architecture is the most common and useful model** for understanding where all technical components fit in information systems
- All devices have a unique **MAC address**; on the internet they get an **IP address**, and human-readable names are stored in the **domain name server**
- Addresses clients use are increasingly **fully qualified names** including the protocol, e.g., `http://web.simmons.edu/index.html`
- End users send data to servers (**GET** or **POST**); servers respond and send data back
- There are many kinds of servers (web, database, application, print, …)
- 📚 For the **history of the internet and the World Wide Web**: review the resources and recommended videos on Moodle

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| **Client** | A computer/device that requests a service from a server (e.g., your laptop or phone using a browser) |
| **Server** | A computer-based system that provides a service to many connected clients |
| **Two-tier architecture** | Client/server architecture: presentation layer on the client, data layer on the server |
| **Three-tier architecture** | Client + application server + database server |
| **N-tier (multi-tier) architecture** | Client(s) + multiple specialized servers (web, database, application, etc.) |
| **HTTP** | Hypertext Transfer Protocol — the protocol used for client-server communication on the web |
| **HTTPS** | Secure HTTP — packets are encrypted between client and server |
| **GET** | HTTP command: client requests a resource from the server |
| **POST** | HTTP command: client sends data (e.g., a filled-out form) to the server |
| **Request / Response** | Client sends a request; server returns a response (web page, data, file, or a hand-off to another server) |
| **Packet** | Unit of data transmission on the internet, consisting of a header and a body |
| **Web form** | Client-side interface for sending data to a server (built with HTML/CSS) |
| **MAC address** | Fixed, unique physical address of a network device, in hexadecimal separated by colons |
| **IP address** | Address assigned to a device on the internet so servers can locate it |
| **IPv4** | Older IP format: four octets (e.g., 192.168.0.10); 2³² addresses — no longer sufficient |
| **IPv6** | Newer, longer hexadecimal IP format; supports almost unlimited addresses |
| **ISP** | Internet Service Provider (e.g., Verizon) — assigns your IP address |
| **DHCP** | Protocol that dynamically generates IP addresses on the fly |
| **DNS (domain name server)** | Server that maps human-readable domain names to IP addresses |
| **Hexadecimal** | Base-16 number system using digits 0–9 and letters a–f |
| **Port** | Number identifying a specific connection point on a server |
| **Cloud** | Remote servers that sync data between client and server (e.g., Dropbox, Google Drive) |
| **Apache** | A very commonly used web server |

---

## Quick Review Questions

1. Using the library reference desk analogy, who is the client and who is the server?
2. What distinguishes a two-tier architecture from a three-tier architecture? What makes an architecture "n-tier"?
3. What is the difference between the HTTP **GET** and **POST** commands? Which one is used when you submit a login form?
4. Walk through the full request–response cycle that happens when you log in to Gmail and see your inbox.
5. Why is HTTPS preferred over HTTP? What problem does it solve?
6. What is the difference between a MAC address and an IP address? Which one changes and which is fixed?
7. Why was IPv6 introduced? Roughly how many addresses does IPv4 support?
8. What does a domain name server do when you type www.bpl.org into your browser?
9. Identify the five parts of this URL: `http://www.domain.com:1234/catalog/search?title=cats`
10. Name three kinds of servers that might appear in a multi-tier architecture.
