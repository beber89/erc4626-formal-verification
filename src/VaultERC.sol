/// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.0;

import {ERC20} from "solmate/tokens/ERC20.sol";
import {ERC4626} from "solmate/tokens/ERC4626.sol";
import {Owned} from "solmate/auth/Owned.sol";

contract VaultERC is Owned, ERC4626 {
    constructor(address _asset) 
        Owned(msg.sender)
        ERC4626(ERC20(_asset), "Vault Wrapper", "4626") 
        
    {  }


    function totalAssets() public view override returns (uint256) {
        return asset.balanceOf(address(this));
    }
}