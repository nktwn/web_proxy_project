# Web Proxy Project

## Created by:
1. Nurkhat Sergaziyev
2. Zhenis Talipov
3. Zhamil Kassymkhanov

## Overview
A multi-threaded proxy server implemented in Python that supports HTTP and HTTPS connections using the CONNECT method. The server handles requests, filters content, blocks specific IP addresses, caches responses, and logs requests for monitoring.

## Project Structure

The Groupie Tracker Filters project is structured as follows:

```
/web_proxy_project
├── cache.py           # caching module to store HTTP responses temporarily
├── config.py          # configuration settings for proxy server
├── logger.py          # logging module for requests and errors
├── main.py            # main proxy server file
├── security.py        # content filtering and IP blocking logic
└── stats.py           # module to collect request statistics

```

## Objective

1. Build a functional HTTP/HTTPS proxy server.
2. Implement request caching for improved efficiency.
3. Introduce content filtering and IP blocking for security.
4. Log all requests and responses for monitoring.
5. Add request statistics for analytical purposes.

## Usage

1. Run the server: `python3 main.py`
2. Configure your browser to use the proxy:
   - Host: 127.0.0.1
   - Port: 8080
3. Visit websites through the proxy to test its functionality.

## Features

1. HTTP and HTTPS Support
   - Handles HTTP requests and creates tunnels for HTTPS connections using the CONNECT method.
2. Caching
   - Stores frequently accessed HTTP responses temporarily to reduce load on target servers.
3. Content Filtering
   - Blocks specific keywords from appearing in responses.
4. IP Blocking
   - Rejects requests from specific IP addresses listed in the configuration.
5. Logging
   - Logs all incoming requests and errors into proxy.log for debugging and monitoring.
6. Statistics Collection
   - Tracks the number of requests processed per domain.