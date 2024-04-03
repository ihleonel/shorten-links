import { expect, test } from 'vitest'
import { shortener } from '../utilities/shortener'

test('should shorten a link', () => {
  expect(shortener('link')).toBe('link')
})
