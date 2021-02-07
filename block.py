# to check: file run itself or got imported
# condition-> if run_itself: true else false
import json


# function: to create a block
def write_block():
    data = {
        "borrower": "Joma",
        "lender": "Viktor",
        "amount": 1000,
        "prev_block": {
            "hash": "",
            "filename": ""
        },
    }

    with open("test", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write("\n")


# function: to check the integrity of data


#  main driver
def main():
    write_block()


if __name__ == "__main__":
    main()
