name = IRuby.input 'Enter your name'

result = IRuby.form do 
  input :username
  password :password
  button
end

result = IRuby.popup 'Please enter your name' do 
  input
  button
end

result = IRuby.popup 'Confirm' do 
  text 'Are you sure you want to continue?'
  cancel 'No'
  button 'Yes'
end

result = IRuby.form do
  input :username
  password :password
end

result = IRuby.form do 
  input :name, label: 'Please enter your name'
  cancel 'None of your business!'
  button :submit, label: 'All done'
end

result = IRuby.form do 
  checkbox :one, 'Fish', 'Cat', 'Dog', default: 'Fish'
  checkbox :many, 'Fish', 'Cat', 'Dog', default: ['Cat', 'Dog']
  checkbox :all, 'Fish', 'Cat', 'Dog', default: true
  button :submit, label: 'All done'
end

result = IRuby.form do 
  date :birthday
  date :today, default: Time.now
  button
end

result = IRuby.form do 
  IRuby::Input::Button::COLORS.each_key do |color|
    button color, color: color
  end
end

result = IRuby.form do 
  text 'Enter email addresses, one per line (use shift+enter for newlines)'
  textarea :emails
end

result = IRuby.form do 
  html { h1 'Choose a Stooge' }
  text 'Choose your favorite stooge'
  select :stooge, 'Moe', 'Larry', 'Curly'
  button
end

result = IRuby.form do 
  select :stooge, 'Moe', 'Larry', 'Curly'
  select :stooge, 'Moe', 'Larry', 'Curly', default: 'Moe'
  multiple :stooges, 'Moe', 'Larry', 'Curly', default: true, size: 3
  multiple :stooges, 'Moe', 'Larry', 'Curly', default: ['Moe','Curly']
  button
end

result = IRuby.form do 
  radio :children, *(0..12), label: 'How many children do you have?'
  checkbox :gender, 'Male', 'Female', 'Intersex', label: 'Select the genders of your children'
  button
end

IRuby.form do 
  file :avatar, label: 'Choose an Avatar'
  button :submit
end

result = IRuby.form do 
  html { h1 'The Everything Form' }
  text 'Marvel at the strange and varied inputs!'
  date
  file
  input :username
  password
  textarea
  radio *(1..10)
  checkbox 'Fish', 'Cat', 'Dog', label: 'Animals'
  select :color, *IRuby::Input::Button::COLORS.keys
  cancel                     
  button    
end

