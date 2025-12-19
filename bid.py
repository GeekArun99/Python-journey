def highest_bidder(Bids):
      highest_bidder=" "
      highest_bid=0
      for bidder in Bids:
            if(Bids[bidder]>highest_bid):
                  highest_bid = Bids[bidder]
                  highest_bidder= bidder
      print(f"Highest bid is {highest_bid} made by {highest_bidder}")
      print(Bids)
            
Bids={}
Bidding= True
while Bidding is True:
      unser_name =input("Enter user name to Bid : ")
      user_bid = int(input("Enter bidding amount : "))
      Bids[unser_name]=user_bid

      #Still there are any bidders left..?
      bidders =input("Still there are nay biddes pending to bid..? Type Yes or No : ").lower()
      print("\n" * 100)
      if (bidders == "no"):
            Bidding = False
            highest_bidder(Bids)
      else:
            Bidding = True

