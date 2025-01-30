// SPDX-License-Identifier: agpl-3.0
pragma solidity ^0.8.0;

import {ERC20} from "solmate/tokens/ERC20.sol";

// with mint
contract MockAssetA is ERC20 {

    constructor(string memory name_, string memory symbol_, uint8 decimals_) 
      ERC20(name_, symbol_, decimals_) {
    }

 
    function transfer(address to, uint256 amount) public override returns (bool) {
        balanceOf[msg.sender] -= amount;

        balanceOf[to] += amount;

        emit Transfer(msg.sender, to, amount);

        return true;
    }

    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        uint256 allowed = allowance[from][msg.sender]; // Saves gas for limited approvals.

        if (allowed != type(uint256).max) allowance[from][msg.sender] = allowed - amount;

        balanceOf[from] -= amount;
        balanceOf[to] += amount;

        emit Transfer(from, to, amount);

        return true;
    } 
}