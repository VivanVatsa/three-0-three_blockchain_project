# three-0-three: *minimalistic-x-blockchain-x-concept-x-project*

**BLOCKCHAIN DEMO**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://three-0-three.herokuapp.com"><img src="https://img.icons8.com/windows/2x/heroku.png" alt="drawing" width="35" align="center"><img src="https://img.icons8.com/cotton/2x/three-way-direction.png" alt="drawing" width="70" align="center">
</a>


> **a simple decentralized blockchain web-app: PoC{Proof-of-Concept} of a decentral blockchain.**

> **learning about blockchain technology, by creating one!**

### BlockChain Concepts: Behind-the-Scenes
#### What's BlockChain? <a href=""><img src="https://img.icons8.com/wired/2x/blockchain-technology.png" alt="drawing" width="50" align="center"></a>

> **Blockchain** is nothing more than a simple list of records or as buzzwords explain, the ***blocks*** which are linked through cryptographic techniques.
* 3 ingredients that makes a blockchain:

        1. Cryptographic Hash of the previous block
        2. The timestamp
        3. The transaction data (or any other info to be decentralised)

- The concept of decentralisation makes blockchain *immutable*, so no single block can be changed/altered without making changes to all subsequent blocks.
- Conclusively, Understand the concept of **Blockchain as a protocol for inter-node communication & validating new blocks.**


> FUN FACT: YOU CAN RUN THIS APPLICATION ON YOUR LOCAL MACHINE @ ```localhost:5000```
<a href=""><img src="https://img.icons8.com/ios/2x/laptop--v2.gif" alt="drawing" width="35" align="right"></a>

> do these steps: {PTR -> always use virtual_environment} 

```bash
# for python virtual environment
pip install virtualenv

# creating virtual environment
python -m venv <name-of-your-virtual-environment>

# to activate the virtual environment
<name-of-virtualenv>\Scripts\activate.bat
```

```bash
# after setting up virtualenv
# CLONE THIS REPO IN GITHUB CLI AS
gh repo clone https://github.com/VivanVatsa/three-0-three

# install the required libraries to run this app
# open CMD/PowerShell/Bash in the same directory, where clone and....
pip install -r requirements.txt

# run the app.py 
python .\app.py
```
```bash
# voila, the app is hosted on your local machine @localhost:5000 (or your machine local port available)
```


### Magic-in-Making <a href=""><img src="https://img.icons8.com/ios/2x/laptop-settings--v3.gif" alt="drawing" width="50" align="center"></a>
#### What steps I took...
##### 1. Visualized the working of a blockchain:
![BlockChain](https://github.com/VivanVatsa/three-0-three/blob/main/assets/blockchain_diag.png)
-----------------------

##### 2. Created python blocks & checked integrity of the block:
![int_1](https://github.com/VivanVatsa/three-0-three/blob/main/assets/block_int.png) ![int_2](https://github.com/VivanVatsa/three-0-three/blob/main/assets/block_ok.png) ![int_3](https://github.com/VivanVatsa/three-0-three/blob/main/assets/block_chg.png)
-----------------------

##### 3. Using Flask API created the Web UI:
> **WEB UI**
![main](https://github.com/VivanVatsa/three-0-three/blob/main/assets/web_ui_main.png)

> **ENTERING DATA**
![info_ent](https://github.com/VivanVatsa/three-0-three/blob/main/assets/added_info.png) 

> **CHECKING BLOCKCHAIN**
![block_check](https://github.com/VivanVatsa/three-0-three/blob/main/assets/check_block.png)


### Tools-Tape <a><img src="https://img.icons8.com/ios/2x/swiss-army-knife--v2.gif" alt="drawing" width="50" align="center"></a>

> All development done on **Python Virtual Environment**

> Python Version: 3.9.1
##### For Creating Blocks:
- Libraries Used:

        os
        json
        hashlib
##### For Creating Flask API:
- Libraries Used:
        
        flask
        render_template
        requests

*used little bit of **HTML** for webpage minimal design*

*project hosted on [**heroku**](https://three-0-three.herokuapp.com)*

-----------------------
> this application is open-source add your contributions & suggestions and feel free to discuss ideas @ [Discussions](https://github.com/VivanVatsa/three-0-three/discussions).


made with [❤️].
