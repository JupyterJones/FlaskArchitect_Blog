names = ["jome tyler","joe smith","time jones","tytyt sisi"]

smith_names = names.select do |name|
  name.include?("smith")
end
>> ["joe smith"]

require 'sqlite3'

# Open a database
db = SQLite3::Database.new "todo.db"

# Create a table
rows = db.execute <<-SQL
  create table if not exists todos (
    id integer primary key,
    task varchar(255)
  );
SQL

# Insert some data
tasks = [
  ["Wash the car"],
  ["Buy groceries"],
  ["Finish homework"],
  ["Take out the trash"],
]

tasks.each do |task|
  db.execute("insert into todos (task) values (?);", task)
end

# Read the data
puts "All tasks:"
db.execute("select * from todos") do |row|
  puts row
end


require 'sqlite3'

# Open a database
db = SQLite3::Database.new "todo.db"

# Create a table
rows = db.execute <<-SQL
  create table if not exists todos (
    id integer primary key,
    task varchar(255)
  );
SQL

# Insert some data
tasks = [
  ["Wash the car"],
  ["Buy groceries"],
  ["Finish homework"],
  ["Take out the trash"],
]

tasks.each do |task|
  db.execute("insert into todos (task) values (?);", task)
end

# Read the data
puts "All tasks:"
db.execute("select * from todos") do |row|
  puts row
end


gem install sqlite3


# Gemfile

gem 'sqlite3'
bundle install

system("ls")

output = system("ls")

output = %x[ls]

system("gem 'sqlite3")

system("gem install sqlite3")

output = %x[gem install sqlite3]

require 'bundler/setup'

gem 'sqlite3'
bundle install



