control 'upgrade-system' do
        title 'Ensure `apt-get upgrade -y` is already executed'
        describe command('apt-get update; apt-get -qqs upgrade') do
                its('stdout') { should_not match /.*Inst.*Security.* | .*Security.*Inst.*/ }
        end
end

control 'operating-system' do
        title 'Ensure Non-Alpine based Image'
        describe os.family do
          it { should_not eq 'alpine' }
        end
end
