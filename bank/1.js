const MONTHS = {
  january: 1, february: 2, march: 3,    april: 4,
  may: 5,     june: 6,     july: 7,     august: 8,
  september: 9, october: 10, november: 11, december: 12,
};

function toBuddhistEra(day, month, year) {
  const monthNumber = MONTHS[month.toLowerCase()];
  const buddhistYear = year + 543;
  return `${day}/${monthNumber}/${buddhistYear}`;
}

const [day, month, year] = process.argv.slice(2);
console.log(toBuddhistEra(Number(day), month, Number(year)));
