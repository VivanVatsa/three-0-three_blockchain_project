# to check: file run itself or got imported
# condition-> if run_itself: true else false
import json
import os
import hashlib

# name of blockchain is hardcoded several times
# so making a global variable

BLOCKCHAIN_DIR = "blockchain/"


def get_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block, "rb") as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()


# function: to ch   eck the integrity of data
def check_integrity():
    # get the directory of the files in the block
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    print(files)


# function: to create a block
def write_block(borrower, lender, amount):

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    data = {
        "borrower": borrower,
        "lender": lender,
        "amount": amount,
        "prev_block": {
            "hash": get_hash(prev_block),
            "filename": prev_block
        },
    }

    current_block = BLOCKCHAIN_DIR + str(blocks_count + 1)

    with open(current_block, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write("\n")
        # f.write(text)
        # f.writable


#  main driver
def main():
    # write_block(borrower="Ashika", lender="cole", amount=100)
    check_integrity()
    # output
    # ["1.json", "10", "11", "12", "2", "3", "4", "5", "6", "7", "8", "9"]
    #


if __name__ == "__main__":
    main()
