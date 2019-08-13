#!/usr/bin/env ruby
require "socket"
require "highline/import"

class FileClient
  def initialize(ip, port)
    @socket = TCPSocket.new(ip, port)

    request
  end

  def request
    puts "KSL FILE READER"
    puts "=" * 25
    filename = ask "[+] Input Filename -> "
    if File.exists? filename
      puts "[!] File #{filename} is available."
      puts "[!] File size is #{File.size(filename)} byte."
      ans = ask "[?] Do you want to upload this file? (Y/n) "
      if ans.upcase == 'Y'
        @socket.send ans.upcase, 0
        loop do
          res = @socket.recv(1024)

          if res == 'req_file_info'
            @socket.send filename + '|' + File.size(filename).to_s, 0
          elsif res == 'req_file'
            File.open(filename, 'rb') do |file|
              buff = file.read
              @socket.send buff, 0
            end
          else
            puts "=" * 25
            puts res
          end

          break if res.nil? or res == ""
        end
      else
        puts "[!] Upload has been cencel!"
      end
    else
      puts "[!] File doesn't available!"
    end
  end
end

if __FILE__ == $0
  # FileClient.new('127.0.0.1',31337)
  # FileClient.new('172.17.0.2',31337)
  FileClient.new('0.0.0.0',31337)
end
