NOW=date +%F_%H-%M-%S
echo "snapshot https://www.amazon.com/ starting $NOW"
torsocks wkhtmltopdf https://www.amazon.com/ amazon.pdf