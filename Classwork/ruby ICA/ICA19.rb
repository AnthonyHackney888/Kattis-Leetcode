=begin
author: Anthony Hackney
=end

class Account

  def initialize(account_balence)
    @account_balence = account_balence
  end
  
  def account_balence
    @account_balence
  end
  
  def account_balence=(account_balence)
    @account_balence = account_balence
  end
  
  def withdraw(amount)
  end
  def deposit(amount)
  end
  
end

class SavingsAccount < Account
  def initialize(account_balence)
    super
  end
  def withdraw(amount)
    new_balence = account_balence - amount
	if new_balence >= 0
	  self.account_balence = new_balence
	end
  end
  
  def deposit(amount)
    new_balence = account_balence + amount
	self.account_balence = new_balence	
  end
end
class CheckingAccount < Account
  @@overdraft = BigDecimal('35')
  def initialize(account_balence)
    super
  end
  def overdraft
    @@overdraft
  end
  def withdraw(amount)
    new_balence = account_balence - amount
	
	if amount > account_balence
	   account_balence - (overdraft + amount)
	   self.account_balence = new_balence
	end
	
	if new_balence >= 0
	  self.account_balence = new_balence
	end
  end
  
  def deposit(amount)
    new_balence = account_balence + amount
	self.account_balence = new_balence	
  end
end
Check = BigDecimal('100.00')
savings = SavingsAccount.new(Check)
puts savings.withdraw(25)