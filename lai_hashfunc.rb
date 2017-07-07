require "CSV"
require "pry"
require "digest"
BUCKET = 80806

def mod_hash(n)  # 0.5372
  n % BUCKET
end

def square_mod_hash(n)  # 0.2592
  (n ** 2) % BUCKET
end

def md5_mod_hash(n) # 0.6012
  Digest::MD5.hexdigest(n.to_s).to_i(16) % BUCKET
end

def sha1_mod_hash(n) # 0.6021
  Digest::SHA1.hexdigest(n.to_s).to_i(16) % BUCKET
end

buckets = Array.new(BUCKET) { 0 }
collision_count = 0

CSV.foreach("../sql-2.csv") do |row|
  id = if row[0][0] == "b"
         ("1" + row[0].tr("b","")).to_i
       else
         ("2" + row[0].tr("r","")).to_i
       end
  bucket_id = sha1_mod_hash(id)
  if buckets[bucket_id] != 0
    collision_count += 1
  end
  buckets[bucket_id] += 1
end

puts "collision count : #{collision_count}"
puts "used buckets number : #{buckets.reject{|b| b==0}.count}"

binding.pry

a = 0
