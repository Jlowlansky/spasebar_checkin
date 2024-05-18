import time
import random
from web3 import Web3
from eth_account import Account

# ABI контракта
abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"AccessControlBadConfirmation","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"bytes32","name":"neededRole","type":"bytes32"}],"name":"AccessControlUnauthorizedAccount","type":"error"},{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"AddressEmptyCode","type":"error"},{"inputs":[],"name":"AlreadyCreated","type":"error"},{"inputs":[],"name":"AlreadyMemberOfSquare","type":"error"},{"inputs":[],"name":"CanNotApprove","type":"error"},{"inputs":[],"name":"CanNotMintTwice","type":"error"},{"inputs":[],"name":"CanNotTransfer","type":"error"},{"inputs":[],"name":"ECDSAInvalidSignature","type":"error"},{"inputs":[{"internalType":"uint256","name":"length","type":"uint256"}],"name":"ECDSAInvalidSignatureLength","type":"error"},{"inputs":[{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"ECDSAInvalidSignatureS","type":"error"},{"inputs":[{"internalType":"address","name":"implementation","type":"address"}],"name":"ERC1967InvalidImplementation","type":"error"},{"inputs":[],"name":"ERC1967NonPayable","type":"error"},{"inputs":[],"name":"ExceedMaxSupply","type":"error"},{"inputs":[],"name":"FailedInnerCall","type":"error"},{"inputs":[],"name":"InsufficientStakingAmount","type":"error"},{"inputs":[],"name":"InvalidInitialization","type":"error"},{"inputs":[],"name":"InvalidNonce","type":"error"},{"inputs":[],"name":"InvalidSignature","type":"error"},{"inputs":[],"name":"InvalidSquare","type":"error"},{"inputs":[],"name":"InvalidUser","type":"error"},{"inputs":[],"name":"InvalidValue","type":"error"},{"inputs":[],"name":"KickOutDisabled","type":"error"},{"inputs":[],"name":"NotInitializing","type":"error"},{"inputs":[{"internalType":"address","name":"member","type":"address"},{"internalType":"uint256","name":"square","type":"uint256"}],"name":"NotMemberOfSquare","type":"error"},{"inputs":[],"name":"NotSquareOwner","type":"error"},{"inputs":[],"name":"OnlyProtoshipOwner","type":"error"},{"inputs":[],"name":"OnlySpacebarService","type":"error"},{"inputs":[],"name":"OnlySquareNFTContract","type":"error"},{"inputs":[],"name":"OnlySquareOwner","type":"error"},{"inputs":[],"name":"SignatureExpired","type":"error"},{"inputs":[],"name":"TokenLocked","type":"error"},{"inputs":[],"name":"TransferFailed","type":"error"},{"inputs":[],"name":"UUPSUnauthorizedCallContext","type":"error"},{"inputs":[{"internalType":"bytes32","name":"slot","type":"bytes32"}],"name":"UUPSUnsupportedProxiableUUID","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"timestamp","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"newStreak","type":"uint256"}],"name":"CheckedIn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":True,"internalType":"uint256","name":"squareId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minStaking","type":"uint256"},{"indexed":False,"internalType":"string","name":"signatureId","type":"string"}],"name":"CreateSquare","type":"event"},{"anonymous":False,"inputs":[],"name":"EIP712DomainChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint64","name":"version","type":"uint64"}],"name":"Initialized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":False,"internalType":"uint256","name":"randomSeed","type":"uint256"},{"indexed":True,"internalType":"bytes32","name":"raffleId","type":"bytes32"}],"name":"RaffleEntered","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":True,"internalType":"address","name":"account","type":"address"},{"indexed":True,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bool","name":"enabled","type":"bool"}],"name":"SetKickOutEnabled","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"duration","type":"uint256"}],"name":"SetSignatureDuration","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"signer","type":"address"}],"name":"SetSigner","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"maxSupply","type":"uint256"}],"name":"SetSquareMaxSupply","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"uint256","name":"squareId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"minStaking","type":"uint256"}],"name":"SetSquareMinStaking","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"mintPrice","type":"uint256"}],"name":"SetSquareMintPrice","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"vault","type":"address"}],"name":"SetVault","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"newOwner","type":"address"},{"indexed":True,"internalType":"uint256","name":"fromSquareId","type":"uint256"},{"indexed":True,"internalType":"uint256","name":"toSquareId","type":"uint256"}],"name":"TransferOwner","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"user","type":"address"},{"indexed":True,"internalType":"uint256","name":"fromSquareId","type":"uint256"},{"indexed":True,"internalType":"uint256","name":"toSquareId","type":"uint256"},{"indexed":False,"internalType":"enum SpacebarServiceV2.TransferType","name":"transferType","type":"uint8"}],"name":"TransferSquare","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"inputs":[],"name":"BLAST","outputs":[{"internalType":"contract IBlast","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"CHECK_IN_WINDOW","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"COOLDOWN_PERIOD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"CREATE_SQUARE_PARAMS_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"JOIN_SQUARE_PARAMS_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINT_AND_CREATE_SQUARE_PARAMS_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PROTOSHIP_NFT","outputs":[{"internalType":"contract IERC721","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SERVICE_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"STAKE_REGISTRY","outputs":[{"internalType":"contract IEthStakeRegistry","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TRANSFER_SQUARE_PARAMS_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"UPGRADE_INTERFACE_VERSION","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"afterStake","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"afterUnstake","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"beforeStake","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"beforeUnstake","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"calculateRaffleId","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"checkIn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"squareId","type":"uint256"},{"internalType":"uint256","name":"minStaking","type":"uint256"},{"internalType":"string","name":"signatureId","type":"string"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint256","name":"nonce","type":"uint256"}],"internalType":"struct SpacebarServiceV2.CreateSquareParams","name":"params","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"createSquare","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"eip712Domain","outputs":[{"internalType":"bytes1","name":"fields","type":"bytes1"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"version","type":"string"},{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"address","name":"verifyingContract","type":"address"},{"internalType":"bytes32","name":"salt","type":"bytes32"},{"internalType":"uint256[]","name":"extensions","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"enterRaffle","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getRaffleInfo","outputs":[{"internalType":"bool","name":"canEnter","type":"bool"},{"internalType":"bytes32","name":"lastRaffleId","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getUserCheckInStatus","outputs":[{"internalType":"uint256","name":"lastCheckIn","type":"uint256"},{"internalType":"uint256","name":"streak","type":"uint256"},{"internalType":"bool","name":"canCheckIn","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"hasMinted","outputs":[{"internalType":"bool","name":"hasMinted","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"defaultAdmin","type":"address"},{"internalType":"address","name":"serviceAdmin","type":"address"},{"internalType":"contract IBlast","name":"blast","type":"address"},{"internalType":"address","name":"blastPoints","type":"address"},{"internalType":"contract IEthStakeRegistry","name":"stakeRegistry","type":"address"},{"internalType":"contract IERC721","name":"protoshipNFT","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract ISquareNFT","name":"_squareNFT","type":"address"},{"internalType":"address","name":"signer_","type":"address"},{"internalType":"address payable","name":"vault_","type":"address"},{"internalType":"uint256","name":"squareMaxSupply_","type":"uint256"},{"internalType":"uint256","name":"squareMintPrice_","type":"uint256"},{"internalType":"address","name":"nftReserve","type":"address"},{"internalType":"uint256","name":"reserveAmount","type":"uint256"}],"name":"initializeV2","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"squareId","type":"uint256"}],"name":"isSquareCreated","outputs":[{"internalType":"bool","name":"isCreated","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"squareId","type":"uint256"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint256","name":"nonce","type":"uint256"}],"internalType":"struct SpacebarServiceV2.JoinSquareParams","name":"params","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"joinSquare","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"kickOutEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"members","type":"address[]"},{"internalType":"uint256","name":"squareId","type":"uint256"}],"name":"kickOutMembers","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"members","type":"address[]"},{"internalType":"uint256[]","name":"squareIds","type":"uint256[]"}],"name":"kickOutMembersByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"lastParticipationTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"minStaking","type":"uint256"},{"internalType":"string","name":"signatureId","type":"string"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint256","name":"nonce","type":"uint256"}],"internalType":"struct SpacebarServiceV2.MintAndCreateSquareParams","name":"params","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"mintAndCreateSquare","outputs":[{"internalType":"uint256","name":"squareId","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proxiableUUID","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"callerConfirmation","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"enabled","type":"bool"}],"name":"setKickOutEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"setSignatureDuration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newSigner","type":"address"}],"name":"setSigner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxSupply","type":"uint256"}],"name":"setSquareMaxSupply","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"squareId","type":"uint256"},{"internalType":"uint256","name":"minStaking","type":"uint256"}],"name":"setSquareMinStaking","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"mintPrice","type":"uint256"}],"name":"setSquareMintPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"newVault","type":"address"}],"name":"setVault","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"signatureDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"signer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"squareMaxSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"squareId","type":"uint256"}],"name":"squareMinStaking","outputs":[{"internalType":"uint256","name":"minStaking","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"squareMintPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"squareNFT","outputs":[{"internalType":"contract ISquareNFT","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"from","type":"uint256"},{"internalType":"uint256","name":"to","type":"uint256"},{"internalType":"uint256","name":"timestamp","type":"uint256"},{"internalType":"uint256","name":"nonce","type":"uint256"}],"internalType":"struct SpacebarServiceV2.TransferSquareParams","name":"params","type":"tuple"},{"internalType":"bytes","name":"signature","type":"bytes"}],"name":"transferSquare","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"userSquareId","outputs":[{"internalType":"uint256","name":"squareId","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"vault","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"}]


# Адрес контракта
contract_address = '0x5ff315aA82a8B2B435f866d20ECD46959999bDcD'

# Адрес узла Ethereum
w3 = Web3(Web3.HTTPProvider('https://rpc.blast.io'))

# Функция для чтения приватных ключей из файла
def read_private_keys(filename):
    with open(filename, 'r') as file:
        private_keys = file.readlines()
    return [key.strip() for key in private_keys]
# Функция для генерации случайного лимита газа
def get_random_gas_limit(min_gas, max_gas):
    return random.randint(min_gas, max_gas)
# Приватные ключи аккаунтов
private_keys = read_private_keys('private_keys.txt')

# Перемешиваем приватные ключи
random.shuffle(private_keys)

# Создание экземпляра контракта
contract = w3.eth.contract(address=contract_address, abi=abi)

# Метод ID для функции checkIn()
method_id = '0x183ff085'

# Создание транзакции для каждого аккаунта
successful_accounts = []  # Список для успешно выполненных кошельков


# Создание транзакции для каждого аккаунта
for private_key in private_keys:
    account = Account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(account.address)
    tx = contract.functions.checkIn().build_transaction({
        'chainId': 81457,  # Идентификатор сети Ethereum
        'gas': get_random_gas_limit(62000, 75000),  # Лимит газа
        'gasPrice': w3.eth.gas_price,  # Цена газа
        'nonce': nonce,  # Нонс
    })
    
    # Подпись и отправка транзакции
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # Ожидание подтверждения транзакции
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Транзакция от аккаунта {account.address} успешно отправлена и подтверждена. Hash: {tx_hash.hex()}")
    
    # Добавление успешно выполненных кошельков в список
    successful_accounts.append(account.address)

    # Пауза на случайное количество секунд от 45 до 150
    random_delay = random.uniform(100, 550)
    rounded_delay = round(random_delay)
    print(f"Ожидаю {rounded_delay} сек. перед следующим аккаунтом")
    time.sleep(rounded_delay)

# Запись успешно выполненных кошельков в файл
with open('successful.txt', 'w') as file:
    for account_address in successful_accounts:
        file.write(f"{account_address}\n")
