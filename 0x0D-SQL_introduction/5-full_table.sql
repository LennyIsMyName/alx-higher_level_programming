-- Prints a table description.

USE hbtn_0c_0;
GO

DECLARE @TableName NVARCHAR(128) = 'first_table';
PRINT 'TableName: ' + @TableName;

PRINT 'Colomns:';
EXEC sp_colomns @TableName;

PRINT 'Primary Key:';
EXEC sp_pkeys @TableName;
