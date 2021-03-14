# Top X cryptocurrencies

This tool helps you parse the top X cryptocurrencies for every week since 2013 as posted on https://coinmarketcap.com/historical

Grab the files with:  
`wget -w 70 -r -l 1 --include-directories=historical https://coinmarketcap.com/historical/`  
In the generated historical folder run:  
`topcryptoccurencies.py */index.html`

All the fields you see on https://coinmarketcap.com/historical are available for the Python script to parse. By default it will consider the top 10 cryptocurrencies, ignoring Tether, and print the number of weeks in the top 10 plus the last week it was in the top 10. Today this output is:

Coin,Top 10 Week Count,Last Top 10 Date
Bitcoin,411,20210307  
Litecoin,410,20210307  
XRP,397,20210307  
Ethereum,292,20210307  
Dash,185,20171231  
Bitcoin Cash,185,20210221  
Stellar,162,20210228  
Dogecoin,130,20210207  
EOS,130,20200816  
MaidSafeCoin,123,20170423  
Peercoin,118,20160508  
Binance Coin,106,20210307  
Monero,101,20200112  
Cardano,93,20210307  
Nxt,91,20160814  
BitShares,89,20170625  
NEM,84,20180211  
Namecoin,80,20151129  
Bitcoin SV,80,20201101  
Ethereum Classic,61,20171105  
IOTA,50,20180902  
Feathercoin,32,20131208  
Chainlink,32,20210307  
Novacoin,31,20131124  
Neo,30,20180429  
TRON,30,20190721  
Augur,29,20170514  
Terracoin,28,20131110  
Steem,28,20170122  
Omni,27,20140706  
Polkadot,27,20210307  
Banx,25,20151011  
Primecoin,22,20131215  
Devcoin,18,20130929  
Tezos,17,20200531  
PayCoin,15,20150329  
BitShares PTS,14,20140406  
Freicoin,13,20130728  
Quark,13,20140223  
Counterparty,13,20141214  
BlackCoin,12,20140720  
Crypto.com Coin,12,20201004  
WorldCoin,11,20131229  
Bytecoin,11,20170528  
Lisk,10,20160731  
Factom,9,20160501  
Auroracoin,8,20140420  
The DAO,8,20160717  
CHNCoin,7,20130623  
Stratis,7,20170730  
Megacoin,6,20140112  
DigixDAO,5,20160612  
Bullion,4,20131117  
Waves,4,20170604  
Infinitecoin,3,20130901  
Golem,3,20170528  
BitConnect,3,20171029  
Bitcoin Gold,3,20171210  
Mincoin,2,20131103  
Digitalcoin,2,20130714  
Emercoin,2,20160131  
Yacoin,1,20130707  
SpainCoin,1,20140316  
Aphroditecoin,1,20140323  
Startcoin,1,20140615  
XCurrency,1,20140706  
NuShares,1,20150118  
TRMB,1,20151108  
HyperSpace,1,20160403  
PIVX,1,20170416  
Storeum,1,20200315  
TAGZ5,1,20200405  
Uniswap,1,20210307  
