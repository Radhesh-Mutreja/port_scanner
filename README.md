# port_scanner
Nmap Port Scanner with GUI
Overview

This project is a Python-based port scanner that uses Nmap to scan a target host and display open ports and services.
A Tkinter GUI was added to make the tool easier to use, while preserving the original scanning code exactly as provided.

The GUI captures the output of the original print() statements and displays them in a scrollable window.

Features

Uses python-nmap as a wrapper for Nmap

Performs service and script scanning (-sV -sC)

Simple graphical interface built with Tkinter

Non-blocking scan execution using threading

Original scanning logic remains unchanged

Requirements

Windows OS

Python 3.10 or higher

Nmap (installed separately)

Python Libraries

python-nmap

tkinter (included with Python)
