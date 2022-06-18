// SPDX-License-Identifier: Unlicensed

pragma solidity >=0.8.0 <0.9.0;

contract Ownable {

    address public father;

    modifier onlyFather() {
        require(msg.sender == father);
        _;
    }
}