# to check: file run itself or got imported
# condition-> if run_itself: true else false
import json


# function: to create a block
def write_block(borrower, lender, amount):
    data = {
        "borrower": borrower,
        "lender": lender,
        "amount": amount,
        "prev_block": {
            "hash": "",
            "filename": ""
        },
    }

    current_block ='blockchain/' + 

    with open("test", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write("\n")
        # f.write(text)
        # f.writable


# function: to check the integrity of data
# def check_integrity():
#     pass


#  main driver
def main():
    write_block(borrower="Ashika", lender="cole", amount=100)


if __name__ == "__main__":
    main()
