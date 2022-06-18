// SPDX-License-Identifier: Unlicensed

pragma solidity >=0.8.0 <0.9.0;

import "./ownable.sol";
import "./safemath.sol";

contract Bank is Ownable {

    mapping(address => uint) public allowances;
	
	event Deposit(address indexed depositor, uint amount);
	event Grant(address indexed sender, address indexed spender, uint amount);
	event Withdraw(address indexed withdrawer, uint amount);

    using SafeMath for uint;

    constructor(address _father) {
        father = _father;
    }

    function deposit() external payable onlyFather {
        // require(msg.sender == father);
        require(msg.value > 0, "Deposit amount should be greater than zero.");
		emit Deposit(msg.sender, msg.value);
    }

    function grantAllowance(address _spender, uint _amount) external onlyFather {
        // require(msg.sender == father);
        require(_spender != father, "Father can't be the spender");
        require(_spender != address(0), "Spender is not a valid account");
        allowances[_spender] = allowances[_spender].add(_amount);
		emit Grant(msg.sender, _spender, _amount);
    }

    function withdraw(uint _amount) external {
        // require(msg.value == 0);
        require(msg.sender != father, "Father cannot withdraw the amount");
        address payable beneficiary = payable(msg.sender);
        require(_amount <= allowances[msg.sender], "You can't withdraw more than the permitted limit");
        require(_amount > 0, "Withdrawal amount should be greater than zero.");
        allowances[msg.sender] = allowances[msg.sender].sub(_amount);
        beneficiary.transfer(_amount);
		emit Withdraw(msg.sender, _amount);
    }

    function allowance() external view returns(uint) {
        return allowances[msg.sender];
    }
}