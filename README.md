# ipgrep

    usage:
      ipgrep [file ...]
      or
      [command] | ipgrep

**ipgrep** scans one or more input files (or `stdin` when called without arguments) for valid IPv4 or IPv6 addresses and prints the result. It accepts text files in any format (plaintext, JSON, YAML, etc.) so long as the files contain IPs separated by a delimiter it can recognize (i.e., any whitespace character and any punctuation character other than `.` or `:`).

This Python3 implementation is heavily based on the [Go version by princebot](https://github.com/princebot/ipgrep).  
There is however a slight difference in handling delimiters — see the 127.0.0.1 example below.

These are all valid inputs:

	10.10.10.2 https://webserver.com
	{"ip": "172.16.2.84"}
	log -> time=13:10, event=foo, addr=192.168.0.2, desc="a foo went bar"
	IP address 8.8.8.8 is for Google DNS.
	Google DNS also supports IPv6: 2001:4860:4860::8888

**ipgrep** would extract `10.10.10.2`, `172.16.2.84`, `192.168.0.2`, `8.8.8.8`, and `2001:4860:4860::8888` from the above.

princebot's original version intentionally excluded IPs that are directly preceded or followed by a `.` or `:`, e.g. in

	There’s no place like 127.0.0.1.

When this Python implementation encounters such a case, it does some guesswork and tries to parse the string minus (1) its last, (2) its first, or (3) both its and first and last characters. It will return the first of these attempts that returns a valid IP (if any).

Following the MIT license of its Go "parent" implementation, this utility is also released under the MIT license. See the `LICENSE` file included in this repo.
