// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import "@testing-library/jest-dom/extend-expect"
import '@testing-library/jest-dom'
module.exports = {
    testPathIgnorePatterns: ['<rootDir>/node_modules', '<rootDir>/dist'], // might want?
    moduleNameMapper: {
        '@components(.*)': '<rootDir>/src/components$1' // might want?
    },
    moduleDirectories: ['<rootDir>/node_modules', '<rootDir>/src'],
    setupFilesAfterEnv: ['<rootDir>/src/jest-setup.ts'] // this is the KEY
    // note it should be in the top level of the exported object.
};