#!/bin/bash
echo "User: $(whoami)"
echo "Date: $(date)"
echo "Directory: $(pwd)"
echo "Disk usage:"; df -h / | tail -1
echo "Memory:"; free -h | head -2
