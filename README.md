# Good Morning Sir

This is a simple Python script that greets the user based on the local time and the gender they have input. Depending on the time of day, the program will say "Good Morning", "Good Afternoon", "Good Evening", or "Good Night". It will also address the user as "Sir" or "Ma'am" based on the gender they provide.

Features

- Greets the user based on the current time.
- Addresses the user as "Sir" or "Madam" based on the gender they input.

Example

If your name is Sanchit and you identify as male, the program will greet you as "Good Morning Sir", "Good Evening Sir", or "Good Night Sir" depending on the time of day. For a female user, it will greet as "Good Morning Ma'am", "Good Evening Ma'am", or "Good Night Ma'am".

Usage

To use this script, simply run it and follow the prompts to enter your name and gender.

```python
Name = input("Enter your name: ")
Gen = input("Enter your gender: ")

import time
timestamp = int(time.strftime('%H'))

if timestamp < 12:
    greeting = "Good Morning"
elif 12 <= timestamp < 17:
    greeting = "Good Afternoon"
elif 17 <= timestamp < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

if Gen == "male":
    title = "Sir"
elif Gen == "female":
    title = "Madam"
else: 
    title = ""

print(f"{greeting}, {Name} {title}")
```

Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sanchitc05/Good-Morning-Sir.git
    ```
2. Navigate to the project directory:
    ```bash
    cd good-morning-sir
    ```
3. Run the script:
    ```bash
    python script.py
    ```

Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Author

[Sanchit Chauhan](https://github.com/sanchitc05)
```

Replace `sanchitc05` with your actual GitHub username. This `README.md` file should give users a clear understanding of what your project does and how to use it.