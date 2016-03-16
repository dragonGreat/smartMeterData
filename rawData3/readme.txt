bus1:PC+fan4
bus2:pc+pad
bus3:pc+hairdryer1
bus4:pc+fan1
bus5:pc+hairdryer2
bus6:pc+phone
bus7:pc+fan2
bus8:pc+hairdryer3
bus9:pc+fan3

bus10:pc(on)+phone(on)+fan1(on)->fan2(on)->fan3(on)->fan4(on)->fan(off)->phone(off)->all(off)
bus11:fan4(on)->phone(on)->phone¹Ø-pc(on)->fan3(on)->fan2£¨on£©->fan1£¨on£©->fan(off)-all(off)
bus12:hairdryer1(on)->pc(on)->pad(on)->hairdryer1£¨off£©->pad(off)->all(off)
bus13:hairdryer1(on)->kettle(on)-hairdryer£¨off£©->all(off)
bus14:kettle+phone
bus15: state(0)- phone(on) - pad(on)-fan1(on)-pad(off)-fan(off)-fan1(on)-phone(off)-pad(on)-phone(off)-off-on-fan(on)-pad(on) -phone(on)-all(off)
        