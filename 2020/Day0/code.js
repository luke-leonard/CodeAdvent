var Person = /** @class */ (function () {
    function Person() {
    }
    Person.prototype.Spend10Dollars = function () {
        this.money -= 10;
    };
    return Person;
}());
var james = new Person();
james.money = 100.00;
james.name = 'james';
