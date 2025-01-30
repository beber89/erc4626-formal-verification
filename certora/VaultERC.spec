
using MockAssetA as AssetA ; 


methods {
    function name() external returns string envfree;
    function symbol() external returns string envfree;
    function decimals() external returns uint8 envfree;
    function asset() external returns address envfree;

    function totalSupply() external returns uint256 envfree;
    function balanceOf(address) external returns uint256 envfree;
    function nonces(address) external returns uint256 envfree;

    function approve(address,uint256) external returns bool;
    function deposit(uint256,address) external;
    function mint(uint256,address) external;
    function withdraw(uint256,address,address) external;
    function redeem(uint256,address,address) external;

    function totalAssets() external returns uint256 envfree;
    function convertToShares(uint256) external returns uint256 envfree;
    function convertToAssets(uint256) external returns uint256 envfree;
    function previewDeposit(uint256) external returns uint256 envfree;
    function previewMint(uint256) external returns uint256 envfree;
    function previewWithdraw(uint256) external returns uint256 envfree;
    function previewRedeem(uint256) external returns uint256 envfree;

    function maxDeposit(address) external returns uint256 envfree;
    function maxMint(address) external returns uint256 envfree;
    function maxWithdraw(address) external returns uint256 envfree;
    function maxRedeem(address) external returns uint256 envfree;

    function permit(address,address,uint256,uint256,uint8,bytes32,bytes32) external;
    function DOMAIN_SEPARATOR() external returns bytes32;

    //// #ERC20 methods
    function _.balanceOf(address) external  => DISPATCHER(true);
    function _.transfer(address,uint256) external  => DISPATCHER(true);
    function _.transferFrom(address,address,uint256) external => DISPATCHER(true);

    function AssetA.balanceOf(address) external returns uint256 envfree;
    function AssetA.allowance(address, address) external returns uint256 envfree;
    function AssetA.transferFrom(address,address,uint256) external returns bool;

}
   

ghost mathint sumOfBalances {
    init_state axiom sumOfBalances == 0;
}


hook Sstore balanceOf[KEY address a] uint256 newValue (uint256 oldValue)  {
    sumOfBalances = sumOfBalances + newValue - oldValue;
}

hook Sload uint256 val balanceOf[KEY address a]  {
    require sumOfBalances >= val;
}


invariant totalSupplyIsSumOfBalances()
    totalSupply() == sumOfBalances;


