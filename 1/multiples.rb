#!/usr/bin/env ruby
sum = 0
for i in 0..999
   if i % 3 == 0 or i % 5 == 0 then
      sum += i
   end
end
puts sum