require 'sinatra'

get '/hello/:x' do 
  logger.info "#{params[:x]}"
  y = string[]
  5.times do 
    logger.info "#{y+=1}"
  end

  "Hello #{params[:x]}!"
end

