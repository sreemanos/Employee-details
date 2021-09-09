//Employee Management system
//Author - Sreeman
//Created on - 24-8-2021

using System;
using System.Text.RegularExpressions;

namespace myproject
{
    public class Employee
	{
		public void NameConditionCheck(string name)
		{
			try
			{
				Space(name);
				Numerics(name);
				SpecialCharacters(name);
				Repetition(name);
				LessWords(name);
			}
			catch (NameHasSpaceException e)
			{
				Console.WriteLine(e.Message);
				ValidateName();
			}
			catch (NameHasNumericsException e1)
			{
				Console.WriteLine(e1.Message);
				ValidateName();
			}
			catch (NameHasSpecialCharacterException e2)
			{
				Console.WriteLine(e2.Message);
				ValidateName();
			}
			catch (NameHasRepetitionException e3)
			{
				Console.WriteLine(e3.Message);
				ValidateName();
			}
			catch (NameHasLessWordsException e4)
			{
				Console.WriteLine(e4.Message);
				ValidateName();
			}

		}
		public void ValidateName()
		{
			Console.WriteLine("Enter Employee Name: ");
			string name = Console.ReadLine();
			NameConditionCheck(name);
		}
				
		public void Space(string name)
		{
			for (int length = 0; length < name.Length; length++)
			{
				bool space;
				space = Char.IsWhiteSpace(name[length]);
				if (space == true)
				{
					throw (new NameHasSpaceException("\nEnter name without spaces"));
				}
			}
		}
		public void Numerics(string name)
		{
			for (int length = 0; length < name.Length; length++)
			{
				bool number;
				number = Char.IsDigit(name[length]);
				if (number == true)
				{
					throw (new NameHasNumericsException("\nEnter name without numbers"));
				}
			}
		}
		public void SpecialCharacters(string name)
		{
			for (int length = 0; length < name.Length; length++)
			{
				bool specialcharacter;
				specialcharacter = Char.IsLetterOrDigit(name[length]);
				if (specialcharacter != true)
				{
					throw (new NameHasSpecialCharacterException("\nEnter name without special characters"));
				}
			}
		}
		public void Repetition(string name)
		{
			for (int length = 1; length < name.Length - 1; length++)
			{
				if ((name[length - 1] == name[length]) && (name[length] == name[length + 1]))
				{
					throw (new NameHasRepetitionException("\nEnter name without repetition"));
				}
			}
		}
		public void LessWords(string name)
		{
			if (name.Length < 3)
			{
				throw (new NameHasLessWordsException("Enter name with 3 or more characters"));
			}
			else
			{
				Console.WriteLine("\nEmployee name: " + name);
			}

		}
		public void ValidateEmpID(int Count)
		{
			string EmployeeID = "ACE000" + Count;
			Console.WriteLine("\nEmployee ID: " + EmployeeID);

		}
		
	 
		public void ValidateEmail()
		{
			Console.WriteLine("\nEnter employee Email Id: ");
			string EmailId = Console.ReadLine();
			string Pattern = @"\A(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)\Z";

			//check first string
			if (Regex.IsMatch(EmailId, Pattern))
			{
				//if email is valid
				Console.WriteLine("\nEmail ID: " + EmailId);
			}
			else
			{
				Console.WriteLine("\n"+EmailId + " is not a valid Email address");
				ValidateEmail();
			}
		}
		public void ValidatePhoneNo()
		{
			Console.WriteLine("\nEnter the phone number: ");
			string Phone = Console.ReadLine();
			int flag = 0;

			if (Phone.Length == 10)
			{
				for (int k = 0; k < Phone.Length; k++)
				{
					if (Phone[k] - 48 >= 0 && Phone[k] - 48 <= 5 && k == 0)
					{
						flag = 2;
						Console.WriteLine("\nPhone number dont start with 0 to 4. Enter valid phone num.");
						ValidatePhoneNo();

					}
					if (Phone[k] - 48 >= 0 && Phone[k] - 48 <= 9)
					{
						flag = 1;
						continue;
					}
					else
					{
						flag = 0;

						break;
					}
				}
			}
			else
			{
				Console.WriteLine("\nEnter only 10 digits.");
				flag = 1;
				ValidatePhoneNo();
			}
			if (flag == 0 && Phone.Length == 10)
			{
				Console.WriteLine("\nYou have entered valid phone number.");
			}
		}


		public void ValidateQualification()
		{
			Console.WriteLine("\nQualifications : \nA)B.E ECE \nB)B.E EEE \nC)B.E CSE  \nD)B.TECH IT\n ");
			Console.WriteLine("\nPick your qualification-(A or B or C or D): ");
			char Qualification;
			Qualification = Convert.ToChar(Console.ReadLine());
			switch (Char.ToLower(Qualification))
			{
				case 'a':
					Console.WriteLine("\nQualification : B.E ECE");
					break;
				case 'b':
					Console.WriteLine("\nQualification : B.E EEE");
					break;
				case 'c':
					Console.WriteLine("\nQualification : B.E CSE");
					break;
				case 'd':
					Console.WriteLine("\nQualification : B.TECH IT");
					break;
				default:
					Console.WriteLine("\nInvalid option");
					ValidateQualification();
					break;
			}
		}
		
	}
	public class Salary:Employee
    {
		public void ValidateSalary()
		{
			Console.WriteLine("\nEnter employee salary: ");
			int Salary = Convert.ToInt32(Console.ReadLine());
			if (Salary != 0)
			{
				Console.WriteLine("\nSalary: " + Salary);
			}
			else
			{
				Console.WriteLine("\nEnter Valid Salary");
				ValidateSalary();
			}
		}
	}
	public class NameHasSpaceException : Exception
	{
		public NameHasSpaceException(string message) : base(message)
		{
		}
	}
	public class NameHasNumericsException : Exception
	{
		public NameHasNumericsException(string message) : base(message)
		{
		}
	}
	public class NameHasSpecialCharacterException : Exception
	{
		public NameHasSpecialCharacterException(string message) : base(message)
		{
		}
	}
	public class NameHasRepetitionException : Exception
	{
		public NameHasRepetitionException(string message) : base(message)
		{
		}
	}
	public class NameHasLessWordsException : Exception
	{
		public NameHasLessWordsException(string message) : base(message)
		{
		}
	}
	public class Validation
	{
		Validation()
        {
			int count = 1;
			char choice;

			while (count != 0)
			{
				Salary s = new Salary();
				s.ValidateEmpID(count);
				s.ValidateName();
				s.ValidateEmail();
				s.ValidatePhoneNo();
				s.ValidateQualification();
				s.ValidateSalary();
				Console.WriteLine("\nDO YOU WANT TO CONTINUE (Y/N)?= ");
				choice = Convert.ToChar(Console.ReadLine());
				if (Char.ToUpper(choice) == 'Y')
				{
					count++;
				}
				else
				{
					Console.WriteLine("\nTHANK YOU FOR ENTERING YOUR DETAILS");
					count = 0;
				}
			}
		}
		public static void Main(string[] args)
		{
			Validation v = new Validation();
			
		}
		}
}






