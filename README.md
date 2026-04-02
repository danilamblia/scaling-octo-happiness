# scaling-octo-happiness

## Wi-Fi brute force

I had reset my Wi-Fi router and then found that the factory sticker was destroyed. This Python script helps me determine the correct last digit of the password.

To use the script, you need a `passwords.txt` file that contains a variety of passwords.

## Requirements

- Python 3
- Python modules: `pywifi` and `time`
- Root or Administrator rights

On Linux, to create a password file with a numeric sequence, I use:

```bash
seq 0 10 > passwords.txt
```

## Usage

```bash
git clone https://github.com/danilamblia/scaling-octo-happiness
cd scaling-octo-happiness/
```

**MAKE OR MOVE YOUR FILE password.txt HERE!**

```bash
sudo python3 scaling-octo-happiness.py
```
