const isUpperCase = c => c >= 65 && c <= 90;
const isLowerCase = c => c >= 97 && c <= 122;

function applyMask(target, mask) {
  const len = Math.max(target.length, mask.length);
  const result = [];

  for (let i = 0; i < len; i++) {
    const targetCode = target.charCodeAt(i);
    const maskCode   = mask.charCodeAt(i);

    const targetIsUpper = isUpperCase(targetCode);
    const targetIsLower = isLowerCase(targetCode);
    const maskIsUpper   = isUpperCase(maskCode);
    const maskIsLower   = isLowerCase(maskCode);

    const bothUpper    = targetIsUpper && maskIsUpper;
    const bothLower    = targetIsLower && maskIsLower;
    const mixedCase    = (targetIsUpper && maskIsLower) || (targetIsLower && maskIsUpper);

    if (bothUpper)       result.push(target[i]);
    else if (bothLower)  result.push(mask[i]);
    else if (mixedCase)  result.push('$');
    else                 result.push('#');
  }

  return result.join('');
}

const [target, mask] = process.argv.slice(2);
console.log(applyMask(target, mask));
