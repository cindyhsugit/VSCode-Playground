const { add } = require('../src/index');

test('adds two numbers', () => {
  expect(add(2, 3)).toBe(5);
});

test('handles negative values', () => {
  expect(add(-1, 4)).toBe(3);
});
