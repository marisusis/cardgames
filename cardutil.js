function Card(suit, value) {
	this.suit = suit;
	this.value = value;
}

Card.values = {
	11: "J",
	12: "Q",
	13: "K",
	1: "A"
}

Card.prototype.getArt = function() {
	art = []
	switch (this.suit) {
		case "H":
		case "S":
		case "D":
		case "C":
			var char = {
				"H": "\u2665",
				"S": "\u2660",
				"D": "\u2666",
				"C": "\u2663"
			}[this.suit];
			var tempArt = Card.templates[this.value];
			art = tempArt.map(function(v) {
				return v.replace(/(o)/gi, char)
			});
			break;
	}
	return art;
}

Card.prototype.print = function() {
	var art = ""
	let artArray = this.getArt();
	for (var i in artArray) {
		art += artArray[i] + "\n"
	}
	console.log(art)
}



Card.templates = {
	1: [" _______",
	"|A      |",
	"|       |",
	"|   o   |",
	"|       |",
	"|______A|"],
	2: [" _______",
	"|2      |",
	"|   o   |",
	"|       |",
	"|   o   |",
	"|______2|"],
	3: [" _______",
	"|3      |",
	"|   o   |",
	"|   o   |",
	"|   o   |",
	"|______3|"],
	4: [" _______",
	"|4      |",
	"| o   o |",
	"|       |",
	"| o   o |",
	"|______4|"],
	5: [" _______",
	"|5      |",
	"| o   o |",
	"|   o   |",
	"| o   o |",
	"|______5|"],
	6: [" _______",
	"|6      |",
	"| o   o |",
	"| o   o |",
	"| o   o |",
	"|______6|"],
	7: [" _______",
	"|7      |",
	"|  o o  |",
	"| o o o |",
	"|  o o  |",
	"|______7|"],
	8: [" _______",
	"|8      |",
	"| o o o |",
	"|  o o  |",
	"| o o o |",
	"|______8|"],
	9: [" _______",
	"|9      |",
	"| o o o |",
	"| o o o |",
	"| o o o |",
	"|______9|"],
	10: [" _______",
	"|10 o   |",
	"| o o o |",
	"| o o o |",
	"| o o o |",
	"|_____10|"]
}

var card = new Card(process.argv[2], process.argv[3]);
console.log(process.argv)
card.print()
